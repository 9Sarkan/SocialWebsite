from django.contrib import admin
from .models import ChangePasswordToken, NUser
from django.http import HttpResponse
from django.core import serializers


def export_as_json(ModelAdmin, request, queryset):
    respose = HttpResponse(content_type='Application/json')
    serializers.serialize('json', queryset,stream=respose)
    return respose

export_as_json.short_description = 'export selected item as json'.title()

@admin.register(ChangePasswordToken)
class changepassworktokenpanel(admin.ModelAdmin):
    list_display = ['email', ]
    actions = [export_as_json, ]

@admin.register(NUser)
class nuseradmin(admin.ModelAdmin):
    list_display = ['user', 'number', ]
    actions = [export_as_json, ]

