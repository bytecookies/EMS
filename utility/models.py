from django.db import models

# Create your models here.



class Country(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



class Department(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name






class NatureOfBusiness(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class ProductCatogory(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name


class ProductSubCatogory(models.Model):
    product = models.ForeignKey(ProductCatogory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name



class VenderProductAndService(models.Model):
    name = models.CharField(max_length=255)
   

    def __str__(self) -> str:
        return self.name



class Nationality(models.Model):
    name=models.CharField(max_length=255)
    
class Organization(models.Model):
    name=models.CharField(max_length=255)

   
class HowDidYouGetToKnowAboutINTIMASIA(models.Model):
    name=models.CharField(max_length=255)
