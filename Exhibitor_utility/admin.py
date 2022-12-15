from django.contrib import admin
from .models import ExhibitorDownload , StaticDownload
# Register your models here.

@admin.register(ExhibitorDownload)
class ExhibitorDownloadAdmin(admin.ModelAdmin):
    autocomplete_fields=['exhibitor']
    # pass
    

@admin.register(StaticDownload)
class StaticDownloadAdmin(admin.ModelAdmin):
    pass
    # pass
    
