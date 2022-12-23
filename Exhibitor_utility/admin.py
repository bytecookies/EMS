from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ExhibitorDownload)
class ExhibitorDownloadAdmin(admin.ModelAdmin):
    autocomplete_fields=['exhibitor']
    # pass
    

@admin.register(StaticDownload)
class StaticDownloadAdmin(admin.ModelAdmin):
    pass
    # pass
    
@admin.register(PromotionalCreative)
class PromotionalCreativeAdmin(admin.ModelAdmin):
    autocomplete_fields=['exhibitor']
    # pass
    
@admin.register(FloorPlan)
class FloorPlanAdmin(admin.ModelAdmin):
    pass
    
