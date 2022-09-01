from django.contrib import admin
from .models import Slider, Logo, service_home, team, counter,client_View, about_page
from django.utils.html import format_html
import admin_thumbnails

# Register your models here.
# @admin_thumbnails.thumbnail('Sliderimage')
class Slideradmin(admin.ModelAdmin):
    list_display=('id','name','description','sliderimage')
    list_filter = ['name']
    ordering = ['-name']
    search_fields = ['name','description']

admin.site.register(Slider, Slideradmin)


class serviceadmin(admin.ModelAdmin):
    list_display=('name','short_name')
    list_filter = ['name']
    ordering = ['-name']
    search_fields = ['name']
admin.site.register(service_home,serviceadmin)
admin.site.register(counter)
class Teamadmin(admin.ModelAdmin):
    list_display=('name','position')
    list_filter = ['name']
    ordering = ['name']
    search_fields = ['name']
admin.site.register(team,Teamadmin)
admin.site.register(client_View)


class aboutAdmin(admin.ModelAdmin):
    list_display = ['name','Short_description']
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(about_page,aboutAdmin)