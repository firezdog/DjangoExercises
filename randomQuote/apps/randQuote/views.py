# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    visits = request.session.get('visits', 0)
    visits +=1
    request.session['visits'] = visits
    string = get_random_string(32)
    context = {
        'string': string,
        'visits': visits
    }
    return render(request, 'index.html', context)

def reset(request):
    request.session['visits'] = 0
    return redirect('/')