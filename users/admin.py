from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, notifications
class UserAdmin(BaseUserAdmin):
  fieldsets = (
      (None, {'fields': ('email', 'password')}),
       (('Fees_info'), {'fields': ('total_fees','Paid_fees','remaining_fees',)}),
      (('Personal info'), {'fields': ('username','first_name', 'last_name','phone')}),
      (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('user_info'), {'fields': ('native_name','gender')}),
        
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2','phone','total_fees','Paid_fees','remaining_fees'),
      }),
  )
  list_display = ['email', 'username', 'is_staff', "native_name", "phone",'total_fees','Paid_fees','remaining_fees']
  search_fields = ('email', 'first_name', 'last_name','phone')
  ordering = ('email','phone','first_name' )
  list_per_page = 10
  

admin.site.register(CustomUser, UserAdmin)

class notify(admin.ModelAdmin):
  list_display = ['name', 'created_at', 'updated_at']

admin.site.register(notifications,notify)