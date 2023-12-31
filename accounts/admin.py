from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Parsional info'), {'fields': ('firs_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    
admin.site.register(CustomUser, CustomUserAdmin)