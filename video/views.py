from django.shortcuts import render
from .models import watch_video

# Create your views here.
def video(request):
     videodict= watch_video.objects.filter()
     return render(request,'videos.html',{'videodict':videodict})