# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = []
        if len(postData['course_name']) < 5:
            errors.append("Course name must be more than 5 characters long.")
        if len(postData['course_description']) < 15:
            errors.append("Course description must be more than 15 characters long.")
        return errors
class Course(models.Model):
    course_name = models.CharField(max_length=55)
    creator = models.ForeignKey(User, related_name="courses_created")
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(User, related_name="courses_attended")
    objects = CourseManager()
