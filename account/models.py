from django.db import models
from django.contrib.auth.models import User


class ChangePasswordToken(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    token = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class NUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nuser')
    profile = models.ImageField(verbose_name='Profile Image')
    birthday = models.DateField(verbose_name='Birthday', null=True, blank=True)
    number = models.CharField(verbose_name='Phone number', max_length=16)
    bio = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.email


