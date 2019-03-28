from django.contrib import admin
from .models import *
from django.core import serializers
from django.http import HttpResponse


def export_as_json(ModelAdmin, request, queryset):
    response = HttpResponse(content_type='Application/json')
    serializers.serialize('json', queryset, stream=response)
    return response


export_as_json.short_description = 'export selected items as json'.title()


@admin.register(Post)
class PostAdminPanel(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'date', 'display_categories', )
    list_filter = ('title', 'display_author', 'display_categories', )
    search_fields = ('title', 'display_author', 'body', )
    actions = [export_as_json, ]


admin.site.register(PostCategory)
admin.site.register(Tag)

