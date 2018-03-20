# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from  models import User
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    errors = messages.get_messages(request)
    context = {
        'messages': errors
    }
    return render(request, 'new.html', context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email'].lower()
        User.objects.create(first_name = first, last_name = last, email = email)
        return redirect('/users')

def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'show_user.html', context)

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')

def edit(request, id):
    errors = messages.get_messages(request)
    context = {
        'user': User.objects.get(id=id),
        'errors': errors
    }
    return render(request, 'edit_user.html', context)

def update(request):
    id = request.POST['user']
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse('my_edit',kwargs={'id':id}))
    else:    
        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email'].lower()
        u = User.objects.get(id=id)
        u.first_name = first
        u.last_name = last
        u.email = email
        u.save()
        return redirect('/users')