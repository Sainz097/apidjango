# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()