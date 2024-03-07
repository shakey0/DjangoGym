from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    DOB = models.DateField()
    entry_code = models.CharField(max_length=10)
    membership = models.CharField(max_length=50)

    def __str__(self):
        return f'Client: {self.user.first_name} {self.user.last_name}'
