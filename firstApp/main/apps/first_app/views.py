from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to display list of blogs."
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display form to create new blog."
    return HttpResponse(response)

def create(response):
    return redirect('/')

def show(response, blog_id):
    response = "Placeholder to display blog {}".format(blog_id)
    return HttpResponse(response)

def edit(response, blog_id):
    response = "Placeholder to edit blog {}".format(blog_id)
    return HttpResponse(response)

def destroy(response, blog_id):
    return redirect('/')