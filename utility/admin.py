from django.contrib import admin
from . import models
# Register your models here.


class ProductSubCatogoryINline(admin.TabularInline):
    model = models.ProductSubCatogory
    extra = 1



class ProductCatogoryAdmin(admin.ModelAdmin):
    inlines = [ProductSubCatogoryINline]
    search_fields = ["product_catogory"]



class NatureOfBusinessAdmin(admin.ModelAdmin):
    search_fields = ["nature_of_bussiness"]


class BrandAdmin(admin.ModelAdmin):
    search_fields = ["our_brand"]


class ProductSubCatogoryAdmin(admin.ModelAdmin):
    search_fields = ["product_sub_catogory"]



admin.site.register(models.Designation)
admin.site.register(models.Department)
admin.site.register(models.NatureOfBusiness, NatureOfBusinessAdmin)
admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.VenderProductAndService)
admin.site.register(models.ProductCatogory, ProductCatogoryAdmin)
admin.site.register(models.ProductSubCatogory, ProductSubCatogoryAdmin)
