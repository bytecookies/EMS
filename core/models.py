from django.contrib.auth.models import AbstractUser
from .managers import customUserManager
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    objects = customUserManager()
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    isExhibitor = models.BooleanField(
        _("Exhibitor status"),
        default=False,
    )
    t_n_d = models.BooleanField(
        default=False, verbose_name="Terms & Conditions")
    isVisitor = models.BooleanField(
        _("Visitor status"),
        default=False,
    )
    REQUIRED_FIELDS = []


class Exhibitor(models.Model):
    DEPARTMENT = (
        ("select", ""),
        ("Admin", "Admin"),
        ("Business Development / Sales", "Business Development / Sales"),
        ("Consultant", "Consultant"),
        ("Distribution", "Distribution"),
    )
    BOOTH_TYPE = (
        ("0", ""),
        ("1", "BARE SPACE"),
        ("2", "SHELL SCHEME")
    )
    companyName = models.CharField(max_length=30)
    contactPerson = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    department = models.CharField(
        max_length=30, choices=DEPARTMENT, default='select')
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    boothNumber = models.CharField(max_length=30)
    boothSize = models.IntegerField()
    boothType = models.CharField(
        max_length=30, choices=BOOTH_TYPE, default="0")
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.companyName

    def save(self, *args, **kwargs):
        if self._state.adding:
            print("adding new Exhibitor")
            password = customUserManager().make_random_password()
            user = User.objects.create_exhibitor(
                email=self.email, password=password)
            self.user = user
            print("this is password ", password)
        super().save(*args, **kwargs)


class Vender(models.Model):
    PRODUCT_AND_SERVICEC_OFFER = (
        ("0", ""),
        ("1", "Exhibitions"),
        ("2", "Conference"),
        ("3", "Award Nights"),
        ("4", "Weddings"),
        ("5", "Birthday Parties"),
        ("6", "Celebrations"),
    )
    companyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pinCode = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    website = models.URLField(max_length=200)
    productAndServicecOffer = models.CharField(
        max_length=200, choices=PRODUCT_AND_SERVICEC_OFFER, default="0")
    briefProfile = models.TextField(max_length=400)

    def __str__(self):
        return self.companyName


class VenderContact(models.Model):
    Vender = models.ForeignKey(
        Vender,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=200)
