from django.http import HttpResponse
from django.shortcuts import redirect, render

from testapp.form import EmployeeForm, EmployeeForm2, EmployeePimgForm
from testapp.utils import upload_file


def index(request):
    if request.method == 'POST':
        empForm = EmployeeForm(request.POST)
        if empForm.is_valid():
            #lets do something
            return HttpResponse("good job")
        else:
            return render(request, 'index.html', {'form': empForm})
    else:
        emp = EmployeeForm()
        return render(request, "index.html", {"form": emp})


def index2(request):
    if request.method == 'POST':
        empForm2 = EmployeeForm2(request.POST, request.FILES)
        if empForm2.is_valid():
                        
            #lets do something
            #print (request.FILES['profile_image'])
            upload_file(request.FILES['profile_image'])
            return HttpResponse("good job")
        else:
            return render(request, 'index2.html', {'form': empForm2})
    else:
        emp = EmployeeForm2()
        
    return render(request, "index2.html", {"form": emp})


def index3(request):
    if request.method == 'POST':
        emp = EmployeePimgForm(request.POST, request.FILES)
        if emp.is_valid():
            emp.save()
            return HttpResponse("good job")
        else:
            return render(request, 'index3.html', {'form': emp})
    else:
        emp = EmployeePimgForm()

    return render(request, "index3.html", {"form": emp})
