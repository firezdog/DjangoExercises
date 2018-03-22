from django.conf.urls import url
from . import views


urlpatterns = [
    #main path = /courses/
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^(?P<course_id>\d+)/enroll', views.enroll),
    url(r'^(?P<course_id>\d+)/unenroll', views.unenroll),
    url(r'^(?P<course_id>\d+)/remove', views.remove),
    url(r'^(?P<course_id>\d+)/delete', views.delete),
    url(r'^(?P<course_id>\d+)/show', views.show)
]