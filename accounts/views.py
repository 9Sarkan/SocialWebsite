from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import login_form, change_password_form, ForgetPasswordForm, RegisterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from .models import ChangePasswordToken, NUser
from django.utils.crypto import get_random_string
from django.views import generic


def is_not_auth(user):
    return not user.is_authenticated


@user_passes_test(is_not_auth)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            u = User.objects.create(username=cd['username'], email=cd['email'], password=cd['passwordConf'])
            u.last_name = cd["family"]
            u.first_name = cd['name']
            u.save()
            nu = NUser.objects.create(user=u, number=cd['phone'], birthday=cd['birthday'])
            nu.save()
            login(request, u)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = RegisterForm()
        return render(request, 'account/register.html', context={'form': form})


@user_passes_test(is_not_auth)
def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:                                                    # check username and password
                if user.is_active:                                      # check user status
                    login(request, user)                                # login user
                    return HttpResponseRedirect(reverse('dashboard'))   # redirect to dashboard
                else:
                    return HttpResponse('User is disabled')
            else:
                return HttpResponse('the username or password is invalid')
    else:                                                               # if http method isn't post send form to user
        form = login_form()
    return render(request, 'account/login.html', context={'form': form})


@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def send_rest_password(email):
    if ChangePasswordToken.objects.get(email=email):
        pass
    else:
        token = get_random_string(length=100)
        ChangePasswordToken.objects.create(email=email, token=token)
        # send rest email


@user_passes_test(is_not_auth)
def ForgetPasswordView(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_rest_password(email)
            return render(request, 'account/sent.html')
    else:
        form = ForgetPasswordForm()
    return render(request, 'account/forgetpassword.html', context={'form': form})


def change_password(request, token=None):
    if request.method == 'POST':
        usertoken = ChangePasswordToken.objects.get(token=token)
        if usertoken:
            user = User.objects.get(email=usertoken.email)
            if user:
                form = change_password_form(request.POST)
                if form.is_valid():
                    password = form.cleaned_data['password']
                    user.password = password
                    user.save()
                    usertoken.delete()
                    return redirect(reverse('dashboard'))
            else:
                return redirect(reverse('login'))
    else:
        email = ChangePasswordToken.objects.get(token=token)
        if email:
            context = {'form': change_password_form()}
            return render(request, 'account/change-password.html', context=context)
        return redirect(reverse('login'))   # if token is wrong or not exist


class ProfileView(generic.DetailView):
    model = User
    template_name = 'account/profileSettings.py'

    def get_context_data(self, **kwargs):
        pass
