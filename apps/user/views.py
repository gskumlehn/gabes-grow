from apps.user.forms import LoginForm

from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect

def login(request):
    if request.user:
        if request.user.is_authenticated:
            return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(request, username=form['username'].value(), password=form['password'].value())

            if user is not None:
                auth.login(request, user)
                messages.success(request, "login successful")

                return redirect('index')
            else:
                messages.error(request, "login failed")
                return redirect('login')
    form = LoginForm()

    return render(request, 'user/login.html', {"form": form})

def logout(request):
    auth.logout(request)
    return redirect('index')