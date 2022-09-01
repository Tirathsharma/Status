from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index),
    path('mylogo',views.mylogo),
    path('about',views.about),
    path('services',views.services),
    path('career',views.career),
    path('contact',views.contact),
]