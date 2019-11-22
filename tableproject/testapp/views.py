from django.shortcuts import render
from .models import *
from  .forms import *


from django.http.response import HttpResponse

def employee_view(request):
    if request.method=='POST':
        eform=employee_form(request.POST)
        if eform.is_valid():
            eform.save()
            eform = employee_form()
            return render(request, 'employee.html', {'eform': eform})
        else:
            return HttpResponse('user invalid data')
    else:
        eform=employee_form()
        return render(request,'employee.html',{'eform':eform})
