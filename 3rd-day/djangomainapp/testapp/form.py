

from dataclasses import field, fields

from django import forms

from testapp.models import Employee


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
