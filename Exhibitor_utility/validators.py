import os
from django.core.exceptions import ValidationError

def pdf_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Only PDF file extension is allowed.')

def jpg_file_extension(value):
    
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg','.jpeg','.jpe']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Only JPG file extension is allowed.')

def ai_file_extension(value):
   
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.ai']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Only AI file extension is allowed.')