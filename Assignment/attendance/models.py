from django.db import models
from django.contrib.auth.models import User
from assign_app.models import UserProfileInfo

class Attendance(models.Model):
    username = models.ForeignKey(User, db_column="username", on_delete = models.CASCADE)
    start_time = models.DateTimeField('Time')
    end_time = models.DateTimeField('Time',  blank=True, null=True)
    project_name = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)
    total_time = models.CharField(max_length=100)

    
    # def __str__(self):
    #     return self.project_name, self.task_name, str(self.start_time.date()), str(self.end_time)
