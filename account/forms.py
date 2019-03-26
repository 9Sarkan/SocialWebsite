from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class login_form(forms.Form):
    username = forms.CharField(max_length= 30, widget=forms.TextInput(attrs={'class':"input100", 'type':"text", 'name':"username", 'placeholder':"Username"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':"input100", 'type':"password", 'name':"pass", 'placeholder':"Password"}))


class change_password_form(forms.Form):
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput(attrs={'class':"input100", 'type':"password", 'name':"password", 'placeholder':"Password"}))
    password_conf = forms.CharField(max_length = 50, widget = forms.PasswordInput(attrs={'class':"input100", 'type':"password", 'name':"password_conf", 'placeholder':"Password Confirm"}))

    def clean_password(self):
        data1 = self.cleaned_data['password']
        data2 = self.cleaned_data['password_conf']
        if data1 != data2:
            raise ValidationError('Please check password')
        else:
            return data1


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':"input100", 'type':"text", 'name':"email", 'placeholder':"Email"}))

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.get(email=data):
            return data
        else:
            raise ValidationError('This email does not exist, you can just sing up!')


