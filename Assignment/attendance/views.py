from django.shortcuts import render
from assign_app.forms import UserForm,UserProfileInfoForm
from attendance.forms import AttendanceForm
from attendance.models import Attendance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import redirect

def index(request):
    return render(request,'assign_app/index.html')

def createAttendance(request, id=None):
    print('request: ',request.user, id)
    # if request.user.is_authenticated():
    #     username = request.user.username
    #     userId = request.user.id
    #     print('id:*******',userId, username)
    if request.method == 'POST':
        attendance_form = AttendanceForm(data=request.POST)
        
        if attendance_form.is_valid():
            attendance = attendance_form.save(commit=False)
            attendance.username = request.user
            attendance.save()
            
        else:
            print(attendance_form.errors)
    else:
        attendance_form = AttendanceForm()
    return render(request,'attendance/create.html',
                          {'attendance':attendance_form})


def edit(request, id):  
    attendance = Attendance.objects.get(id=int(id)) 
    return render(request,'attendance/edit.html', {'attendance':attendance})  

    
def update(request, id):  
    attendance = Attendance.objects.get(id=int(id))  
    attendance_form = AttendanceForm(data=request.POST, instance = attendance)
    if request.method == 'POST':
        if attendance_form.is_valid():
            attendance = attendance_form.save(commit=False)
            attendance.project_name = Attendance.objects.values_list('project_name', flat=True).filter(id=int(id))[0]
            attendance.save()
        else:
            print(attendance_form.errors)
    return render(request,'attendance/edit.html', {'attendance':attendance})  


def listAttendance(request):
    context ={} 
    context['noItem'] = True
    try:
        # add the dictionary during initialization 
        context["dataset"] = Attendance.objects.filter(username = request.user) 

        timeX= Attendance.objects.all().values('start_time').filter(end_time__isnull = True, username = request.user).order_by('-start_time')

        context['timer'] = str(timeX[0]['start_time'])
        if len(context["dataset"]) != 0:
            noItem = False

        context['noItem'] = noItem
        print('timer: ',timeX)
        print(context)
    except Exception as e:
        
        print (e)
          
    return render(request, 'attendance/list.html', context)
