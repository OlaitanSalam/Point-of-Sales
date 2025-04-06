from django.contrib import admin
from posApp.models import Store, Products, Sales, salesItems, CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    # Extend the default fieldsets to include 'store' and 'is_superadmin'
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('store', 'is_superadmin')}),
    )
    # When adding a new user, include the custom fields
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('store', 'is_superadmin')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'store', 'is_superadmin', 'is_staff')
    list_filter = ('is_superadmin', 'store')

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(Store)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
# admin.site.register(Employees)
