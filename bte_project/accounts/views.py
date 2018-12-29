from django.shortcuts import render, redirect
from django.contrib import messages
# import models for auth checking to see if user exists
from django.contrib.auth.models import User
# Create your views here.


def register(req):
    # register user
     # dont forget to return a response
    if req.method == 'POST':
        # get form values
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        user_name = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            # check user name if passwords match
            # if username already is in db return an error
            if User.objects.filter(username=username).exists():
                messages.error(req, 'That username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(req, 'That email already exists')
                    return redirect('register')

        else:
            # if passwords do not match for registration
            # send error
            messages.error(req, 'Passwords do not match')
            return redirect('register')
    else:
        return render(req, 'accounts/register.html')


def login(req):
    # login user
    if req.method == 'POST':
        print('submited')
        # dont forget to return a response
        return redirect('register')
    else:
        return render(req, 'accounts/register.html')


def logout(req):
    return redirect('index')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')
