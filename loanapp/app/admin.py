from django.contrib import admin
from django.contrib.auth import get_user_model as User
from .models import Staff, Payments, Client
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


# class UserAdmin(BaseUserAdmin):
#     model = User
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)


admin.site.register(User())
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(Payments)
