from django.shortcuts import render
from . models import Employee
from django.views.generic import View
from django.utils import timezone
from .models import *
from pdf.utils import Render


class Pdf(View):
    def get(self, request):
        employee = Employee.objects.all()
        params = {

            'employee': employee,
            'request': request
        }
        return Render.render('pdf.html', params)

# Create your views here.
def display_view(request):
    employee = Employee.objects.all()
    print(type(employee))
    return render(request,'index.html',{'employee':employee})