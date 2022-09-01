from django.shortcuts import render
from .models import service
from home.models import service_home
# Create your views here.
def ourservice(request,short_name):
     services= service_home.objects.filter(short_name=short_name)
     return render(request,'each_services.html',{'services':services})