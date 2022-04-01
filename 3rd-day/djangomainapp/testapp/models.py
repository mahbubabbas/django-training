from django.db import models
from django.forms import CharField


class Employee(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)

    class Meta:
        db_table = "employee"
