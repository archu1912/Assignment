from django.conf.urls import url
from attendance import views
# SET THE NAMESPACE!
app_name = 'attendance'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^save_attendance/$',views.createAttendance,name='save_attendance'),
    url(r'^edit/(?P<id>[0-9]+)/$',views.edit,name='edit'),
    url(r'^update/(?P<id>[0-9]+)/$',views.update,name='update'),
    url(r'^list_attendance/$',views.listAttendance,name='list_attendance'),
]