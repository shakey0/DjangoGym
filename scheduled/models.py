from django.db import models
from django.contrib.auth.models import User
from classes.models import Class
from instructor.models import Instructor


class Scheduled(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1, blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.RESTRICT)
    instructor = models.ForeignKey(Instructor, on_delete=models.RESTRICT)
    users = models.ManyToManyField(User, related_name='scheduled_users')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, default='TBD')
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.class_id.name} scheduled for {self.start_time}'
