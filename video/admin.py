from django.contrib import admin
from .models import *


# Register your models here.
class  VideoAdmin(admin.ModelAdmin):
    list_display=['name','Video_tag']

admin.site.register(watch_video, VideoAdmin)