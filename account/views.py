from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import login_form
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test, login_required

def is_not_auth(user):
    return not user.is_authenticated

# @user_passes_test(is_not_auth)
def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
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
    return render(request, 'account/login.html', context = {'form': form})

# @login_required
def logout(request):
    logout(request)
    return HttpResponse('Logouted')