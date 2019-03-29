from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<slug>[\w-]+)/$', views.PostView.as_view(), name='PostView'),
]
