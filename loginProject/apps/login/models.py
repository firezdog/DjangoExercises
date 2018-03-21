# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

emailRegex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# Create your models here.
class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = []
        user = User.objects.filter(email=postData['login'])
        if not len(user):
            errors.append("User not found in the database.")
        else:
            db_password = user[0].password
            entered_password = postData['password']
            if not bcrypt.checkpw(entered_password.encode(), db_password.encode()):
                errors.append("Invalid password.")
        return errors
    def registration_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First name should be at least 2 characters.")
        if not postData['first_name'].isalpha():
            errors.append("First name should consist only of alphabetical characters.")
        if len(postData['last_name']) < 2:
            errors.append("Last name should be at least 2 characters.")
        if not postData['last_name'].isalpha():
            errors.append("Last name should consist only of alphabetical characters.")
        if not emailRegex.match(postData['reg_email']):
            errors.append("Email improperly formatted.")
        if len(User.objects.filter(email=postData['reg_email'])):
            errors.append("Email already found in database.")
        if len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not postData['password'] == postData['confirm_password']:
            errors.append("Password and password confirmation do not match.")
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()