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

    class Meta:
        verbose_name='Nature Of Business'
        verbose_name_plural='Nature Of Business'


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class ProductCatogory(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Product Catogory'
        verbose_name_plural='Product Categories'


class ProductSubCatogory(models.Model):
    product = models.ForeignKey(ProductCatogory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Product Sub Catogory'
        verbose_name_plural='Product Sub Categories'


class VenderProductAndService(models.Model):
    name = models.CharField(max_length=255)
   

    def __str__(self) -> str:
        return self.name



class Nationality(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Nationality'
        verbose_name_plural='Nationalities'

    
        
class Organization(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
   
class HowDidYouGetToKnowAboutINTIMASIA(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
            verbose_name='How Did You Get To Know About INTIMASIA'
            verbose_name_plural='How Did You Get To Know About INTIMASIA'
