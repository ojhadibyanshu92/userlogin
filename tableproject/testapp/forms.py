from django import forms
from testapp.models import *

class employee_form(forms.ModelForm):
    class Meta:
        model = Employee_master
        fields = '__all__'