"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
import assign_app.views as assign_view
# from assign_app import views
import attendance
from django.views.generic.base import TemplateView
from django.conf.urls import handler404, handler500

handler404 = 'assign_app.views.noPage'
handler500 = 'assign_app.views.noPage500'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',assign_view.index,name='index'),
    url(r'^special/',assign_view.special,name='special'),
    url(r'^assign_app/',include('assign_app.urls')),
    url(r'^attendance/',include('attendance.urls')),
    url(r'^logout/$', assign_view.user_logout, name='logout'),
    
]
