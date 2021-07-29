from django.db import models
from django.contrib.auth.models import User




class UserSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    email = models.EmailField()
    mobile = models.BigIntegerField()


