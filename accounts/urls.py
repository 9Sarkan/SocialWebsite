from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^Change-Password/(?P<string>[\w\-]+)/$', views.change_password, name='changePassword'),
]
