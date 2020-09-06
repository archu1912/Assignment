from django.shortcuts import render
from assign_app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from attendance.models import Attendance
from django.shortcuts import render
from django.template import RequestContext

def index(request):
    context ={}
    try:
        timeX= Attendance.objects.all().values('start_time', 'project_name', 'task_name').filter(end_time__isnull = True, username = request.user).order_by('-start_time').first()
        print('tasks: ', timeX)
        context['timer'] = str(timeX['start_time'])
        context['project_name'] = str(timeX['project_name'])
        context['task_name'] = str(timeX['task_name'])
        
        isWorking = True
        if context['timer'] == '' or context['timer'] == None:
            isWorking = False
        
        context['isWorking'] = isWorking
    except Exception as e:
        print(e)
    return render(request,'assign_app/index.html',context)

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'assign_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'assign_app/login.html', {})

def noPage(request, *args, **kwargs):
    response = render('assign_app/404.html', {},
                                context_instance=RequestContext(request))
    response.status_code = 404
    return response

def noPage500(request, *args, **kwargs):
    response = render('assign_app/500.html', {},
                                context_instance=RequestContext(request))
    response.status_code = 500
    return response

