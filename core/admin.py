from django import forms
from django.contrib import admin
from django.forms import ModelForm

from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from utility.models import *
from . import models




# Register your models here.


class ExhibitorCreateForm(ModelForm):
    CONTACT_PERSONE_CHOICES = (
        ("1", "Senior Management"),
        ("2", "Key Contact Person"),
    )
    contact_person_type = forms.ChoiceField(choices=CONTACT_PERSONE_CHOICES)

    class Meta:
        model = models.Exhibitor
        fields = ('user', 'companyName', 'contact_person_type', 'contact_person_first_name', 'contact_person_last_name', 'designation',
                  'department', 'phone', 'email', 'boothNumber', 'boothSize', 'boothType')
       

    def save(self, commit=True):
        obj = super().save(commit=False)
        # do you logic here for example:
        if (self.data.get('contact_person_type')=='1'):
            print(self.data.get('contact_person_type'))
            obj.senior_person_first_name = obj.contact_person_first_name
            obj.contact_person_first_name = None

            obj.senior_person_last_name = obj.contact_person_last_name
            obj.contact_person_last_name = None

            obj.senior_designation = obj.designation
            obj.designation = None
            
            obj.senior_department = obj.department
            obj.department = None
            
            obj.senior_phone = obj.phone
            obj.phone = None
            
            obj.senior_email = obj.email
            obj.email = None
            

        print(obj.nature_of_bussiness) 
        obj.contactPerson="Piyush"

        if commit:
            # Saving your obj
            obj.save()
        return obj

class ExhibitorChangeForm(ModelForm):
    
    class Meta:
        model = models.Exhibitor
        fields = '__all__'
   


class venderContactInline(admin.TabularInline):
    model = models.VenderContact
    extra = 1





@admin.register(User)
class UserAdmin(BaseUserAdmin):

    ordering = ['email']
    readonly_fields = ['date_joined']
    list_display = ("email", "isExhibitor", "is_active", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Action"),
            {
                "fields": (
                   
                  
                    "t_n_d",
                    "participation_form",
                   
                ),
            },
        ),
        
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "isExhibitor",
                    "isVisitor",
                    "is_staff",
                    
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


@admin.register(models.Exhibitor)
class ExhibitorAdmin(admin.ModelAdmin):

    readonly_fields = ['user']
   
  
    autocomplete_fields = ["nature_of_bussiness",
                           "product_catogory", "product_sub_catogory", "our_brand"]
    list_display = ('companyName', 'contact_person_first_name',
                    'boothSize', 'boothType', 'boothNumber')
    # form = ExhibitorChangeForm

    # def add_view(self, request, form_url='', extra_context=None):
    #     self.form = ExhibitorCreateForm

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     self.form = ExhibitorChangeForm

    add_form = ExhibitorCreateForm
    view_form = ExhibitorChangeForm

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults.update({
                'form': self.add_form,
            })
        else:
            defaults.update({
                'form': self.view_form
            })
        defaults.update(kwargs)
        return super(ExhibitorAdmin,self).get_form(request, obj, **defaults)


@admin.register(models.Vender)
class VenderAdmin(admin.ModelAdmin):
    inlines = [venderContactInline]






