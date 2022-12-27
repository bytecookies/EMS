from django.db import models
from core.models import Exhibitor
from .validators import pdf_file_extension, jpg_file_extension,ai_file_extension
# Create your models here.


def generate_jpg_file_name_for_ExhibitorDownload(instance,filename):
    extention=str(instance.file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.exhibitor.companyName).upper()+"-"+str(instance.title.replace(" ","-")).upper()+"."+extention
    print(new_filename)
    return 'images/exhibitor/downloads/EmailSignatures/'+(new_filename)

class ExhibitorDownload(models.Model):
    exhibitor=models.ForeignKey(Exhibitor, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    file=models.FileField(upload_to=generate_jpg_file_name_for_ExhibitorDownload,validators=[jpg_file_extension])

    def __str__(self) -> str:
        return self.exhibitor.companyName
    class Meta:
        verbose_name='Email Signature'
        verbose_name_plural='Email Signatures'


def generate_pdf_file_name(instance, filename):
    extention=str(instance.pdf_file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.title).upper()+"-PDF."+extention
    # print(new_filename)
    return 'images/exhibitor/downloads/EventCreatives/'+(new_filename)

def generate_jpg_file_name_for_StaticDownload(instance, filename):
    extention=str(instance.jpg_file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.title).upper()+"-JPG."+extention
    # print(new_filename)
    return 'images/exhibitor/downloads/EventCreatives/'+(new_filename)
    
    
def generate_ai_file_name(instance, filename):
    extention=str(instance.ai_file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.title).upper() +"-AI."+extention
    # print(new_filename)
    return 'images/exhibitor/downloads/EventCreatives/'+(new_filename)
    
def generate_thumbnail_file_name(instance, filename):
    extention=str(instance.thumbnail_file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.title).upper() +"-THUMBNAIL."+extention
    # print(new_filename)
    return 'images/exhibitor/downloads/EventCreatives/'+(new_filename)

class StaticDownload(models.Model):
    title=models.CharField(max_length=255)
    pdf_file=models.FileField(upload_to=generate_pdf_file_name,validators=[pdf_file_extension])
    jpg_file=models.FileField(upload_to=generate_jpg_file_name_for_StaticDownload,validators=[jpg_file_extension])
    ai_file=models.FileField(upload_to=generate_ai_file_name,validators=[ai_file_extension])
    thumbnail_file=models.FileField(upload_to=generate_thumbnail_file_name,validators=[jpg_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name='Event Creative'
        verbose_name_plural='Event Creatives'


def generate_jpg_file_name_for_PromotionalCreatives(instance, filename):
    extention=str(instance.jpg_file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.exhibitor.companyName).upper().replace(" ","-")+"-JPG."+extention
    print(new_filename+"======")
    return 'images/exhibitor/downloads/PromotionalCreatives/'+(new_filename)


def generate_thumbnail_file_name_for_PromotionalCreatives(instance, filename):
    extention=str(instance.thumbnail_file).split(".")[1]
    
    # Use the instance object to generate a unique file name
    
    new_filename =str(instance.exhibitor.companyName).upper().replace(" ","-") +"-THUMBNAIL."+extention
    print(new_filename)
    return 'images/exhibitor/downloads/PromotionalCreatives/'+(new_filename)



class PromotionalCreative(models.Model):
    exhibitor=models.ForeignKey(Exhibitor,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=255)
    thumbnail_file=models.FileField(upload_to=generate_thumbnail_file_name_for_PromotionalCreatives,validators=[jpg_file_extension])
    jpg_file=models.FileField(upload_to=generate_jpg_file_name_for_PromotionalCreatives,validators=[jpg_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.exhibitor.companyName

    class Meta:
        verbose_name="Promotional Creative"
        verbose_name_plural="Promotional Creatives"


def generate_pdf_file_name_for_FloorPlans(instance, filename):
    extention=str(instance.pdf_file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.title).upper().replace(" ","-")+"-PDF."+extention
    print(new_filename+"============")
    return 'images/exhibitor/downloads/FloorPlans/'+(new_filename)

def generate_thumbnail_file_name_for_FloorPlans(instance, filename):
    extention=str(instance.thumbnail_file).split(".")[1]
    # Use the instance object to generate a unique file name
    new_filename =str(instance.title).upper().replace(" ","-") +"-THUMBNAIL."+extention
    print(new_filename+"++++++++++++++++")
    return 'images/exhibitor/downloads/FloorPlans/'+(new_filename)  


class FloorPlan(models.Model):
    title=models.CharField(max_length=255)
    pdf_file=models.FileField(upload_to=generate_pdf_file_name_for_FloorPlans,validators=[pdf_file_extension])
    thumbnail_file=models.FileField(upload_to=generate_thumbnail_file_name_for_FloorPlans,validators=[jpg_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Floor Plan"
        verbose_name_plural="Floor Plans"
