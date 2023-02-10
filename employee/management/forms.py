from django import forms
from management.models import Employee
from management.models import Company
from management.models import Login

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields="__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"