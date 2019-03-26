from django import forms

class login_form(forms.Form):
    username = forms.CharField(max_length= 30, widget=forms.TextInput(attrs={'class':"input100", 'type':"text", 'name':"username", 'placeholder':"Username"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':"input100", 'type':"password", 'name':"pass", 'placeholder':"Password"}))
