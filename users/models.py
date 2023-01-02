from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from tinymce import models as tinymce_models
from datetime import date

class CustomUser(AbstractUser):  
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique = True)
    native_name = models.CharField(max_length = 5)
    phone=models.CharField(max_length=10,blank=True,null=True)
    total_fees=models.IntegerField(blank=True,null=True)
    Paid_fees=models.IntegerField(blank=True,null=True)
    remaining_fees=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=10,blank=True,null=True)
    session_token=models.CharField(max_length=10,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    
    def __str__(self):
        return "{}".format(self.email)

class notifications(models.Model):
    name = models.CharField(max_length=250)
    Long_description = tinymce_models.HTMLField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'notifications'
        verbose_name_plural = 'notifications'

    def __str__(self):
        return self.name

