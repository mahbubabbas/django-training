from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from ecommapp.forms import UserForm, UserFormsForm
from ecommapp.models import User


# user registration form
def register(req):
    if req.method == 'POST':
        userForm = UserFormsForm(req.POST)
        if userForm.is_valid():
            u = User(
                username=userForm.cleaned_data['username'],
                password=userForm.cleaned_data['password'],
                role='customer'
            )
            u.save()

            return redirect('login')
        else:
            return render(req, "users/register.html", {"form": userForm})

    else:
        userForm = UserFormsForm()
        return render(req, "users/register.html", {"form": userForm})

# user login form


def login(req):
    if req.method == 'POST':
        userForm = UserForm(req.POST)
        if userForm.is_valid():
            try:
                user = User.objects.get(
                    username=userForm.cleaned_data['username'], password=userForm.cleaned_data['password'])
                req.session['user_id'] = user.id

                return redirect('home')

            except User.DoesNotExist:
                return HttpResponse('error...')
        else:
            return render(req, "users/login.html", {"form": userForm})

    else:
        userForm = UserForm()
        return render(req, "users/login.html", {"form": userForm})

# home page


def home(req):
    if 'user_id' in req.session:
        return render(req, "home.html")
    else:
        return redirect('login')


def logout(req):
    try:
        del req.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
