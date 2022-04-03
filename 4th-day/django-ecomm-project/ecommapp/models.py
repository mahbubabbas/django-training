from django import forms
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=200, default='')
    role = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'user'
