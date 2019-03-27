from django.contrib import admin
from .models import ChangePasswordToken


@admin.register(ChangePasswordToken)
class changepassworktokenpanel(admin.ModelAdmin):
    list_display = ['email', ]


