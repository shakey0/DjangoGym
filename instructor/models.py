from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    DOB = models.DateField()
    image = models.ImageField(upload_to='instructors')
    entry_code = models.CharField(max_length=10)
    instr_type = models.CharField(max_length=50)
    desc = models.TextField()
    qualifications = models.JSONField()
    activities = models.JSONField()

    def __str__(self):
        return self.user.username
