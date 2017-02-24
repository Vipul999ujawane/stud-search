from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stud(models.Model):
    roll=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    hall=models.CharField(max_length=10)
    room=models.CharField(max_length=10)
    stat=models.CharField(max_length=100)
