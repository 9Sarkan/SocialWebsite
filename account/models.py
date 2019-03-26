from django.db import models


class ChangePasswordToken(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    token = models.CharField(max_length=200)

    def __str__(self):
        return self.email

