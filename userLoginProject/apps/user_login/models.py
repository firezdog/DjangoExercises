# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

emailRegex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        rep = "First: {}, Last: {}, Email: {}, Age: {}, Created: {}, Updated {}".format(self.first_name, self.last_name, self.email_address, self.age, self.created_at, self.updated_at)
        return rep
        
@receiver(pre_save, sender=User)
def clean(sender, instance, **kwargs):
    if not(len(instance.first_name) or len(instance.last_name)):
        raise ValidationError(_('First and last name fields must be entered.'))
    if not(emailRegex.match(instance.email_address)):
        raise ValidationError(_('Email address must be in the proper format.'))
    elif len(User.objects.filter(email_address=instance.email_address).exclude(id=instance.id)):
        raise ValidationError(_('Email already exists in the database.'))