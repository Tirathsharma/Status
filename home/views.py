from django.http import HttpResponse
from django.shortcuts import render, redirect
from service.models import service
from django.core.mail import send_mail
from .models import Slider, Logo, service_home,team, counter, client_View , about_page

def mylogo(request):
     mylogo= Logo.objects.all()
     return render(request,'base.html',{'mylogo': mylogo})


def index(request):
     sliderdict= Slider.objects.all()
     teamdict= team.objects.all()
     client_Viewdict= client_View.objects.all()
     mylogo= Logo.objects.all()
     counterdict= counter.objects.all()
     service= service_home.objects.all()
     return render(request,'index.html',{
          'dataslider':sliderdict,
          'mylogo': mylogo,
          'service':service,
          'teamdict': teamdict, 
          'counterdict': counterdict, 
          'client_Viewdict': client_Viewdict,
     })

def about(request):
     about= about_page.objects.all()
     return render(request,'about/about.html',{'about':about})

def services(request):
     services= service.objects.all()
     homeservice= service_home.objects.all()
     return render(request,'services/services.html',{'services':services,'service':homeservice})

def career(request):
     return render(request,'career/career.html')

def contact(request):
     if request.method == "POST":
        username=request.POST['Username']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['project_detail']
        budget=request.POST['budget']
        subject = 'welcome to GFG world'
        message = f'Hi {username}, HI thanks for connecting we will soon connect with you.'
        email_from = 'savantinfolabs@gmail.com'
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/')
                
     else:
        return render(request,'contact/contact.html')

     return render(request,'contact/contact.html')