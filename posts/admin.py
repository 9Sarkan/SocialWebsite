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
    # list_display = ('title', 'display_author', 'date', 'display_categories', )
    # list_filter = ('title', 'display_author', 'display_categories', )
    # search_fields = ('title', 'display_author', 'body', )
    list_display = ('title', 'date', )
    list_filter = ('title', )
    search_fields = ('title', 'body', )
    actions = [export_as_json, ]


admin.site.register(PostCategory)
admin.site.register(Tag)


@admin.register(Comment)
class CommentPanel(admin.ModelAdmin):
    list_display = ['user', 'post', 'date', 'delete']
    list_filter = ('post', 'delete', )
    search_fields = ('post', 'user', 'body', )
    actions = [export_as_json, ]

