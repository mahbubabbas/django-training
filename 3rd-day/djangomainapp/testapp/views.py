from django.http import HttpResponse
from django.shortcuts import redirect, render

from testapp.form import EmployeeForm


def index(req):
    if req.method == 'POST':
        empForm = EmployeeForm(req.POST)
        if empForm.is_valid():
            return HttpResponse("good job")
        else:
            return render(req, 'index.html', {'form': empForm})
    else:
        emp = EmployeeForm()
        return render(req, "index.html", {"form": emp})

