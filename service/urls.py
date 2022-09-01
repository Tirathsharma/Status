from django.urls import path, include
from . import views


urlpatterns = [
    path('service/<str:short_name>',views.ourservice)
]