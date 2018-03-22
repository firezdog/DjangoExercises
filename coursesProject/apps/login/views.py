# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
import bcrypt

firstRun = True

# Create your views here.
def index(request):
    global firstRun
    if firstRun:
        request.session['user'] = 0
        firstRun = not firstRun
    errors = messages.get_messages(request)
    context = {
        'errors': errors
    }
    return render(request, 'login/index.html', context)

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error, extra_tags="login")
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['login'])
        request.session['user'] = user[0].id
        return redirect('/success')

def register(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error, extra_tags="registration")
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['reg_email']
        password = request.POST['password']
        pwhash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = pwhash
        )
    return redirect('/')

def success(request):
    if request.session['user'] > 0:
        return redirect('/courses')
    else:
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')