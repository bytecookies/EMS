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



admin.site.register(models.Nationality)
admin.site.register(models.Organization)
admin.site.register(models.HowDidYouGetToKnowAboutINTIMASIA)
admin.site.register(models.Department)
admin.site.register(models.NatureOfBusiness, NatureOfBusinessAdmin)
admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.VenderProductAndService,
                    VenderProductAndServiceAdmin)
admin.site.register(models.ProductCatogory, ProductCatogoryAdmin)
admin.site.register(models.ProductSubCatogory, ProductSubCatogoryAdmin)
