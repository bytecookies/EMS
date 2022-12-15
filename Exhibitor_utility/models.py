from django.db import models
from core.models import Exhibitor
# Create your models here.


class ExhibitorDownload(models.Model):
    exhibitor=models.ForeignKey(Exhibitor, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    file=models.FileField(upload_to='images/exhibitor/downloads')

    def __str__(self) -> str:
        return self.exhibitor.companyName
    


