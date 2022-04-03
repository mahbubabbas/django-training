import profile

from django.db import models
from django.forms import CharField


class Employee(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)

    class Meta:
        db_table = "employee"


class EmployeePimg(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)

    profile_image = models.FileField(blank=True)

    class Meta:
        db_table = "employee_pimg"
