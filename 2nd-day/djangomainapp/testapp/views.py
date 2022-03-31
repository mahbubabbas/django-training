from django.http import HttpResponse
from django.shortcuts import redirect, render

from testapp.form import EmployeeForm


def index(req):
        emp = EmployeeForm()
        return render(req, "index.html", {"form": emp})

