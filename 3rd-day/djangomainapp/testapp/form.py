from dataclasses import field, fields
from tokenize import blank_re
from django import forms

from testapp.models import Employee, EmployeePimg


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def clean(self):
        super(EmployeeForm, self).clean()

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if len(first_name) < 3:
            self._errors['first_name'] = self.error_class(
                ['A min of 3 chars required for first name'])

        if len(last_name) < 3:
            self._errors['last_name'] = self.error_class(
                ['A min of 3 chars required for last name'])

        return self.cleaned_data


class EmployeeForm2(forms.Form):
    first_name = forms.CharField(
        label="Enter first name", max_length=50, required=True)
    last_name = forms.CharField(
        label="Enter last name", max_length=10, required=True)
    email = forms.EmailField(label="Enter Email", required=False)
    profile_image = forms.FileField(required=False)  # for creating file input


class EmployeePimgForm(forms.ModelForm):
    class Meta:
        model = EmployeePimg
        fields = '__all__'
