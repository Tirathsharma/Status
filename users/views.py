from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import CustomUser, notifications
from  video.models import watch_video
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

def signup(request):
    if request.method == "POST":
        username=request.POST['Username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        phone=request.POST['phone']
        gender=request.POST['gender']
        if request.POST['password1'] == request.POST['password2']:
            user = CustomUser.objects.create_user(username=username,password=password1,phone=phone,email=email,gender=gender)
            user.save()
            return redirect('/')
        else:
            return render (request,'user/register.html', {'error':'Password does not match!'})
    else:
        return render(request,'user/register.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'],password = request.POST['password'])
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/dashboard')
        else:
            return render (request,'user/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'user/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return  redirect('login')




@login_required(login_url='login')
def dashboard(request):
    videodict= watch_video.objects.filter()
    notifydict= notifications.objects.all()   
    return render(request,'user/dashboard.html',{'videodict':videodict,'notifydict':notifydict})