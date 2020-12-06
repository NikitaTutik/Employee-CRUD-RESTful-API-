from django import forms
from api.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = 'full_name', 'dep_code', 'phone_number',
        labels = {
            'full_name': 'Full Name',
            'dep_code': "Department Code"
        }
