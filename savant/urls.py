from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import urls
from users import urls



urlpatterns = [
    path('',include('home.urls')),
    path('',include('users.urls')),
    path('',include('service.urls')),
    path('',include('video.urls')),
    path('login/admin', admin.site.urls),
    # path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "BAPM Course"  
admin.site.site_title  =  "BAPM Course"
admin.site.index_title  =  "BAPM Course"