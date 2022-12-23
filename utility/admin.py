from django.contrib import admin
from . import models
# Register your models here.


class ProductSubCatogoryINline(admin.TabularInline):
    model = models.ProductSubCatogory
    extra = 1
    




class ProductCatogoryAdmin(admin.ModelAdmin):
    inlines = [ProductSubCatogoryINline]
    search_fields = ["name"]





class NatureOfBusinessAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class BrandAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class ProductSubCatogoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class VenderProductAndServiceAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class NationalityAdmin(admin.ModelAdmin):
    search_fields = ["name"]
class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    
class HowDidYouGetToKnowAboutINTIMASIAAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ["name"]



admin.site.register(models.Nationality,NationalityAdmin)
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.HowDidYouGetToKnowAboutINTIMASIA,HowDidYouGetToKnowAboutINTIMASIAAdmin)
admin.site.register(models.Department,DepartmentAdmin)
admin.site.register(models.NatureOfBusiness, NatureOfBusinessAdmin)
admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.VenderProductAndService,
                    VenderProductAndServiceAdmin)
admin.site.register(models.ProductCatogory, ProductCatogoryAdmin)
admin.site.register(models.ProductSubCatogory, ProductSubCatogoryAdmin)
