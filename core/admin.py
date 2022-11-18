from django import forms
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from . import models


# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    readonly_fields = ['date_joined']
    list_display = ("email", "isExhibitor", "is_active", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "isExhibitor",
                    "isVisitor",
                    "is_staff",
                    "t_n_d",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


class ExhibitorAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('user', 'companyName', 'contactPerson', 'designation', 'department', 'phone', 'email', 'boothNumber', 'boothSize', 'boothType'),
        }),
    )
    readonly_fields = ['user']
    list_display = ('companyName', 'contactPerson',
                    'boothSize', 'boothType', 'boothNumber')


class venderContactInline(admin.TabularInline):
    model = models.VenderContact


class VenderAdmin(admin.ModelAdmin):
    inlines = [venderContactInline]


admin.site.register(models.Exhibitor, ExhibitorAdmin)
admin.site.register(models.Vender, VenderAdmin)
