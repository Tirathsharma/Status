from django.db import models
from home.models import *

class service(models.Model):
    name = models.CharField(max_length=250)
    backgroud_image = models.ImageField(upload_to='service/', blank=True, null=True)
    Homeserviceimages2 = models.ImageField(upload_to='service/', blank=True, null=True)
    Homeserviceimages3 = models.ImageField(upload_to='service/', blank=True, null=True)
    Heading = models.CharField(max_length=500)
    more_description = tinymce_models.HTMLField()
    # Service_Item = models.ForeignKey(name, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
# Create your models here.
