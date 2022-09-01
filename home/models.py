from django.db import models
from django.utils.safestring import mark_safe
from tinymce import models as tinymce_models
from service.models import *
# Create your models here.
class Logo(models.Model):
    name = models.CharField(max_length=250)
    Logoimage = models.ImageField(upload_to='slider/', blank=True, null=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    sliderimage = models.ImageField(upload_to='slider/', blank=True, null=True)
    
    def __str__(self):
        return self.name

    # def Sliderimage(self):
    #     if self.sliderimage:
    #         return mark_safe('<img src="/media/%s" width"40px" height="40px">'%self.sliderimage)
    #     else:
    #         pass

class service_home(models.Model):
    name = models.CharField(max_length=250)
    short_name=models.SlugField(max_length=200, unique=True)
    Homeserviceimage = models.ImageField(upload_to='service/', blank=True, null=True)
    Short_description = models.CharField(max_length=500)
    Long_description = tinymce_models.HTMLField()
    related = models.ForeignKey(service, on_delete=models.SET_NULL, blank=True,null=True, related_name="related_service")
    # Service_Item = models.ForeignKey(name, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Home service'
        verbose_name_plural = 'Home service'

    def __str__(self):
        return self.name

class team(models.Model):
    name = models.CharField(max_length=250)
    position= models.CharField(max_length=500)
    team_image = models.ImageField(upload_to='team/', blank=True, null=True)

    class Meta:
        verbose_name = 'Our Team'
        verbose_name_plural = 'Our Team'

    def __str__(self):
        return self.name

class counter(models.Model):
    name = models.CharField(max_length=250)
    float_icon = models.CharField(max_length=250)
    counter= models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Counter +'
        verbose_name_plural = 'Counter +'
    

    def __str__(self):
        return self.name

class client_View(models.Model):
    name = models.CharField(max_length=250)
    Long_description = tinymce_models.HTMLField()

    class Meta:
        verbose_name = 'Client Reviews'
        verbose_name_plural = 'Client Reviews'

    def __str__(self):
        return self.name

class about_page(models.Model):
    name = models.CharField(max_length=250)
    short_name=models.CharField(max_length=50)
    background_banner_img = models.ImageField(upload_to='about/', blank=True, null=True)
    about_image= models.ImageField(upload_to='about/', blank=True, null=True)
    Short_description = models.CharField(max_length=500)
    Long_description = tinymce_models.HTMLField()
    # Service_Item = models.ForeignKey(name, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'
    
    def __str__(self):
        return self.name


