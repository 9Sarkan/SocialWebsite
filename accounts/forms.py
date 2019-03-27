from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User

class login_form(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': "input100", 'type': "text", 'name': "username", 'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "input100", 'type': "password", 'name': "pass", 'placeholder': "Password"}))


class change_password_form(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': "input100", 'type': "password", 'name': "password", 'placeholder': "Password"}))
    password_conf = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': "input100", 'type': "password", 'name': "password_conf", 'placeholder': "Password Confirm"}))

    def clean_password(self):
        data1 = self.cleaned_data['password']
        data2 = self.cleaned_data['password_conf']
        if data1 != data2:
            raise ValidationError('Please check password')
        else:
            return data1


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "input100", 'type': "text", 'name': "email", 'placeholder': "Email"}))

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data):
            return data
        else:
            raise ValidationError('This email does not exist, you can just sing up!')


class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(attrs={
        'class': "input100", 'type': "text", 'name': "name", 'placeholder': "Name"}))
    family = forms.CharField(label='Family', max_length=40, widget=forms.TextInput(attrs={
        'class': "input100", 'type': "text", 'name': "family", 'placeholder': "Family"}))
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={
        'class': "input100", 'type': "text", 'name': "username", 'placeholder': "Username"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': "input100", 'type': "password", 'name': "password", 'placeholder': "Password"}))
    passwordConf = forms.CharField(max_length=50, widget = forms.PasswordInput(attrs={
        'class': "input100", 'type': "password", 'name': "password_conf", 'placeholder': "Password Confirm"}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        'class': "input100", 'type': "text", 'name': "email", 'placeholder': "Email"}))
    phone = forms.CharField(label='Phone Number', max_length=16, widget=forms.TextInput(attrs={
        'class': "input100", 'type': "tel", 'name': "phone", 'placeholder': "Phone Number"}))
    birthday = forms.DateField(label='Birthday', widget=forms.TextInput(attrs={
        'class': "input100", 'type': "date", 'name': "birthday", 'placeholder': "Birthday"}))

    def clean_email(self):
        data = self.cleaned_data['email']
        validate_email(data)
        user = User.objects.filter(email=data)
        if user:
            raise ValidationError('This email is exist, you can just try forgot password!')
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if data.isdigit() and data.startswith('0') and len(data) > 10:
            return data
        else:
            raise ValidationError('Phone number is invalid')

    def clean_username(self):
        data = self.cleaned_data['username']
        user = User.objects.filter(username=data)
        if user:
            raise ValidationError('This username is exist, please try another one!')
        return data

    def clean_passwordConf(self):
        data1 = self.cleaned_data['password']
        data2 = self.cleaned_data['passwordConf']
        if data1 != data2:
            raise ValidationError('Please check password')
        else:
            return data1


