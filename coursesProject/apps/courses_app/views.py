# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import Course
from ..login.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.session['user'] > 0:
        errors = messages.get_messages(request)
        user = User.objects.get(id=request.session['user'])
        courses = Course.objects.all()
        context = {
            'errors': errors,
            'courses': courses,
            'user': user
        }
        return render(request, 'courses_app/index.html', context)
    else:
        return redirect('/')

def create(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error, extra_tags="course")
    else:
        course_name = request.POST['course_name']
        course_description = request.POST['course_description']
        creator = User.objects.get(id=request.session['user'])
        Course.objects.create(
            course_name = course_name,
            description = course_description,
            creator = creator
        )
    return redirect('/courses')

def enroll(request, course_id):
    user = User.objects.get(id=request.session['user'])
    course = Course.objects.get(id=course_id)
    course.students.add(user)
    return redirect('/courses')

def unenroll(request, course_id):
    user = User.objects.get(id=request.session['user'])
    course = Course.objects.get(id=course_id)
    course.students.remove(user)
    return redirect('/courses')

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course
    }
    return render(request, 'courses_app/remove.html', context)

def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.POST['remove'] == "Yes":
        course.delete()
    return redirect('/courses')

def show(request, course_id):
    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=request.session['user'])
    context = {
        'course': course,
        'user': user,
        'students': course.students
    }
    return render(request, 'courses_app/show.html', context)