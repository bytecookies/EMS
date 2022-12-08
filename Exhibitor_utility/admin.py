from django.contrib import admin
from .models import ExhibitorDownload
# Register your models here.

@admin.register(ExhibitorDownload)
class ExhibitorDownloadAdmin(admin.ModelAdmin):
    autocomplete_fields=['exhibitor']
    # pass
    
