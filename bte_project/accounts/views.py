from django.shortcuts import render, redirect
from django.contrib import messages, auth
# import models for auth checking to see if user exists
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(req):
    # register user
     # dont forget to return a response
    if req.method == 'POST':
        # get form values
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
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
                    # if all checks are passed
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # for users that are create auto login below
                    # auth.login(req, user)
                    # messages.success(req, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(req, 'You are now registered')
                    return redirect('login')

        else:
            # if passwords do not match for registration
            # send error
            messages.error(req, 'Passwords do not match')
            return redirect('register')
    else:
        return render(req, 'accounts/register.html')

# determines where the user is routed to html

# dont forget to return a response


def login(req):
    # login user
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # if user is found
            auth.login(req, user)
            messages.success(req, 'You are now logged in')
            return redirect('dashboard')

        else:
            messages.error(req, 'Invalid Login credentials')
            return redirect('login')

    else:
        # determines where the user is routed to html
        return render(req, 'accounts/login.html')


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.success(req, 'You have been logged out')
        return redirect('index')


def dashboard(req):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=req.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(req, 'accounts/dashboard.html', context)
