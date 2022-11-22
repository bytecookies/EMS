from django.contrib import admin
from . import models
# Register your models here.


class ProductSubCatogoryINline(admin.TabularInline):
    model = models.ProductSubCatogory
    extra = 1



class ProductCatogoryAdmin(admin.ModelAdmin):
    inlines = [ProductSubCatogoryINline]



admin.site.register(models.Designation)
admin.site.register(models.Department)
admin.site.register(models.NatureOfBusiness)
admin.site.register(models.Brand)
admin.site.register(models.VenderProductAndService)
admin.site.register(models.ProductCatogory, ProductCatogoryAdmin)
admin.site.register(models.ProductSubCatogory)
