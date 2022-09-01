from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('dashboard/',views.dashboard),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
]
