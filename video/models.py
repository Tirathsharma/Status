from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
# Create your models here.
class watch_video(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    img = models.ImageField(upload_to='images_uploaded',null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'video Lactures'
        verbose_name_plural = 'videos Lactures'

    def  Video_tag(self):
        return mark_safe('<video style="margin-top:-10px;" controls src="/../../media/%s" type="video/mp4" width="200" height="200" allowfullscreen/>' % (self.video))  

    def __str__(self):
        return self.name
        return mark_safe('<video style="float:right; top:0;" controls src="/../../media/%s" type="video/mp4" width="200" height="200" allowfullscreen/>' % (self.video))