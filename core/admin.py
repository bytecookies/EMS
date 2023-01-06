from django import forms
from django.contrib import admin
from django.forms import ModelForm

from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from utility.models import *
from . import models




# Register your models here.

                 


class venderContactInline(admin.TabularInline):
    model = models.VenderContact
    extra = 1

class ExhibitorBrnadOrLogoInline(admin.TabularInline):
    model = models.ExhibitorBrandOrCompanyLogo
    extra = 1





@admin.register(User)
class UserAdmin(BaseUserAdmin):

    ordering = ['email']
    readonly_fields = ['date_joined']
    list_display = ("email", "isExhibitor", "is_active", "is_staff")
    search_fields = ('email',)
    list_filter = ('is_staff', 'isExhibitor','isVisitor','is_superuser','is_active')

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





class ExhibitorCreateForm(ModelForm):
    CONTACT_PERSONE_CHOICES = (
        ("1", "Senior Management"),
        ("2", "Key Contact Person"),
    )
    contact_person_type = forms.ChoiceField(choices=CONTACT_PERSONE_CHOICES)
   

    class Meta:
        model = models.Exhibitor
        fields = ('companyName', 'contact_person_type', 'contact_person_first_name', 'contact_person_last_name', 'designation',
                  'department', 'phone', 'email', 'boothNumber', 'boothSize', 'boothType')
        required = ('email')
        exclude = ('user',) 
       

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
        
       
   

@admin.register(models.Exhibitor)
class ExhibitorAdmin(admin.ModelAdmin):
    inlines = [ExhibitorBrnadOrLogoInline]
    readonly_fields = ['user','last_updated','date_created']

    search_fields=['user__email','companyName']

    list_filter=['user__participation_form','user__t_n_d','boothType']
  
    autocomplete_fields = ["nature_of_bussiness",
                           "product_catogory", "product_sub_catogory", "our_brand"]

    list_display = ('companyName', 'user', 'contact_person','senior_person',
                    'boothSize',  'boothNumber')
    list_per_page=10


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
    


    # coputed fields
    @admin.display(ordering='contact_person_first_name')
    def senior_person(self, exhibitor):
        return f" {exhibitor.contact_person_first_name} {exhibitor.contact_person_last_name}"
    
    @admin.display(ordering='senior_person_first_name')
    def contact_person(self, exhibitor):
         return f" {exhibitor.senior_person_first_name} {exhibitor.senior_person_last_name}"





@admin.register(models.Visitor)
class VisitorAdmin(admin.ModelAdmin):
    search_fields=['user__email','organization_name','first_name']
    readonly_fields = ['user']
    list_display = ('user','name','organization_name','type','date')
    list_editable=['type']
    list_filter=['type','user__date_joined']
    autocomplete_fields = ["nationality",
                           "department", "nature_of_business", "product_category","product_sub_category","brand","how_did_you_get_to_know_about_INTIMASIA","product_category_interest","product_sub_category_interest"]

    list_per_page=10
    
    @admin.display(ordering='user__date_joined')
    def date(self, Visitor):
        return Visitor.user.date_joined
      
    @admin.display(ordering='first_name')
    def name(self, Visitor):
        return f" {Visitor.first_name} {Visitor.last_name}"
    
      
@admin.register(models.VisitorIdPassword)
class VisitorIdPasswordAdmin(admin.ModelAdmin):
    readonly_fields = ['visitor','password']
    list_display=['visitor','password']
    
    

@admin.register(models.Vender)
class VenderAdmin(admin.ModelAdmin):
    inlines = [venderContactInline]


@admin.register(models.Meeting)
class MeetingAdmin(admin.ModelAdmin):
    # inlines = [venderContactInline]
    pass

@admin.register(models.MySchedule)
class MyscheduleAdmin(admin.ModelAdmin):
    # inlines = [venderContactInline]
    pass






