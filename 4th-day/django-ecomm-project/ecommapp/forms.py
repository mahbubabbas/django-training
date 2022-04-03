from dataclasses import fields
from django import forms

from ecommapp.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'password',)

        widgets = {
            'password': forms.PasswordInput()
        }


def clean(self):
    super(UserForm, self).clean()

    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

    if len(username) < 3:
        self._errors['username'] = self.error_class(
            ['A min of 3 chars required for username'])

    if len(password) < 3:
        self._errors['password'] = self.error_class(
            ['A min of 3 chars required for password'])

    return self.cleaned_data


class UserFormsForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    confPassword = forms.CharField(
        max_length=100, widget=forms.PasswordInput())

    def clean(self):
        super(UserFormsForm, self).clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confPassword = self.cleaned_data.get('confPassword')

        if len(username) < 3:
            self._errors['username'] = self.error_class(
                ['A min of 3 chars required for username'])

        if len(password) < 3:
            self._errors['password'] = self.error_class(
                ['A min of 3 chars required for password'])

        if (password != confPassword):
            self._errors['confPassword'] = self.error_class(
                ['Confirm password does not match'])

        return self.cleaned_data
