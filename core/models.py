from django.contrib.auth.models import AbstractUser
from .managers import customUserManager
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMultiAlternatives
# from . import utility_func
from phonenumber_field.modelfields import PhoneNumberField
from django.db import  transaction


from utility.models import *
# from core.utility.constants import department, designation
import random

def send_mail(email, password):
   
    htmly = get_template('pages/components/mail/exhibitor_credential.html')

    d = {'email': email, "password": password}

    subject, from_email = 'Your Login Credential', 'Intimasia <no-reply@intimasia.in>'
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(
        subject=subject, from_email=from_email, to=[email],cc=['intimasia.pr@gmail.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def visitor_welcome_mail(email,context):
    print("mail sent")
    htmly = get_template('pages/components/mail/visitor_welcome.html')
    fname=context['fname']
    lname=context['lname']
    subject, from_email = f'Your Online Registration Confirmation - { fname } { lname }', 'Intimasia <no-reply@intimasia.in>'
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(
        subject=subject, from_email=from_email, to=[email],cc=[context['cc']],bcc=['developer@peppermint.co.in'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def unique_id():
    prifix="IM"
    num=random.randrange(1,10**10)
    code = prifix+str(num)
    check=User.objects.filter(registration_id=code)
    if not check:
        return code
    else:
        get_code=unique_id()
        return get_code



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
    participation_form = models.BooleanField(default=False,)
    isVisitor = models.BooleanField(
        _("Visitor status"),
        default=False,
    )
    registration_id=models.CharField(max_length=12, unique=True)
    REQUIRED_FIELDS = []


class Exhibitor(models.Model):
   
    BOOTH_TYPE = (
        ("0", ""),
        ("1", "BARE SPACE"),
        ("2", "SHELL SCHEME")
    )
   
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, primary_key=True)

    # company detail
    companyName = models.CharField(max_length=255)
    address1=models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    company_email=models.EmailField(blank=True, null=True)
    
    # company billing detail
    billing_companyName = models.CharField(
        max_length=255, blank=True, null=True)
    billing_address1 = models.TextField(blank=True, null=True)
    billing_address2 = models.TextField(blank=True, null=True)
    billing_zip = models.CharField(max_length=255, blank=True, null=True)
    billing_city = models.CharField(max_length=255, blank=True, null=True)
    billing_state = models.CharField(max_length=255, blank=True, null=True)
    billing_country = models.CharField(max_length=255, blank=True, null=True)
    company_GST = models.CharField(max_length=255, blank=True, null=True)
    company_PAN = models.CharField(max_length=255, blank=True, null=True)

    # Key contact person
    contact_person_first_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person_last_name = models.CharField(max_length=255, blank=True, null=True)
   
    designation = models.CharField(max_length=200, blank=True, null=True,)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, blank=True, null=True,)
   
    # phone = models.CharField(max_length=12, blank=True, null=True)
    phone = PhoneNumberField( blank=True, null=True)
    email = models.EmailField(blank=False, null=True)

    # Senior Person Details
    senior_person_first_name = models.CharField(
        max_length=255, blank=True, null=True)
    senior_person_last_name = models.CharField(
        max_length=255, blank=True, null=True)
    # senior_designation = models.CharField(
    #     max_length=200, blank=True, null=True, choices=DESIGNATION)
    # senior_department = models.CharField(
    #     max_length=200, blank=True, null=True, choices=DEPARTMENT)
    # senior_designation = models.ForeignKey(
    #     Designation, on_delete=models.PROTECT, related_name="senior_designation")
    senior_designation = models.CharField(
        max_length=200, blank=True, null=True,)
    senior_department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="senior_department",blank=True, null=True,)
        
    senior_phone = PhoneNumberField(blank=True, null=True)
    senior_email = models.EmailField(blank=True, null=True)
    


    # Booth Details
    boothNumber = models.CharField(max_length=255)
    boothSize = models.IntegerField()
    boothType = models.CharField(
        max_length=255, choices=BOOTH_TYPE, default="0")
   
    # Business Classification Details
    nature_of_bussiness=models.ManyToManyField(NatureOfBusiness, blank=True)
    product_catogory=models.ManyToManyField(ProductCatogory,  blank=True)
    product_sub_catogory = models.ManyToManyField(
        ProductSubCatogory, blank=True)
    our_brand = models.ManyToManyField(Brand, blank=True)



    last_updated=models.DateTimeField(auto_now=True, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.companyName
    
  

    def save(self, *args, **kwargs):
        if self._state.adding:
            print("adding new Exhibitor")
            email=self.email if self.email!=None else self.senior_email
            password = customUserManager().make_random_password()
            k = password
            print(k)
            print("this is password gfdgdfgdfgfdgffffffffffffffffffffffffffffffffffffffffffffff", password)
            registration_id=unique_id()
            user = User.objects.create_exhibitor(
                email=email, password=password,registration_id=registration_id)
            self.user = user
            send_mail(password=password, email=email)
        super().save(*args, **kwargs)


class Visitor(models.Model):
    GENDER_CHOICE=(
    ('','-----'),
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
) 
    SUBSCRIBE_TO_INNER_SECRETS=(
        ('Yes','Yes'),
        ('No','No'),
    )
    IS_FIRST_TIME_TO_INTIMASIA=(
        ('Yes','Yes'),
        ('No','No'),
    )
    TYPE=(
        ('','---'),
        ('VIP','VIP'),
        ('NON-VIP','NON-VIP')
    )
       
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, primary_key=True)

    type=models.CharField(max_length=255, choices=TYPE, default='NON-VIP', )
    
    parent_id=models.ForeignKey("self", on_delete=models.CASCADE, null=True,blank=True)



    #First Page Start of Visitor Form
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(choices=GENDER_CHOICE,max_length=255,null=True,blank=True)
    nationality=models.ForeignKey(Nationality,on_delete=models.PROTECT,null=True,blank=True)
    organization_name=models.CharField(max_length=255,null=True,blank=True)
    department=models.ForeignKey(Department,on_delete=models.PROTECT,null=True,blank=True)
    job_title=models.CharField(max_length=255,null=True,blank=True)
    apartment_unit_building_floor_etc=models.TextField(null=True,blank=True)
    street_address=models.TextField(null=True,blank=True)
    zip_code=models.CharField(max_length=255,null=True,blank=True)
    country=models.CharField(max_length=255,null=True,blank=True)
    state=models.CharField(max_length=255,null=True,blank=True)
    town_city_district=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(unique=True)
    cc_email=models.EmailField(blank=True,null=True)
    mobile=PhoneNumberField(null=True,blank=True)
    whatsapp=PhoneNumberField(blank=True, null=True)
    whatsapp_same_as_mobile_or_no_wp=models.BooleanField(blank=True, null=True)
   

    #Second page of visitor form
    nature_of_business=models.ManyToManyField(NatureOfBusiness,null=True,blank=True)
    nature_of_business_others=models.TextField(blank=True,null=True)
    product_category=models.ManyToManyField(ProductCatogory,null=True,blank=True,related_name='product_category')
    product_category_others=models.TextField(blank=True,null=True)
    product_sub_category=models.ManyToManyField(ProductSubCatogory,null=True,blank=True,related_name='product_sub_category')
    product_sub_category_others=models.TextField(blank=True,null=True)
    brand=models.ManyToManyField(Brand,null=True,blank=True)
    brand_others=models.TextField(blank=True,null=True)
    how_did_you_get_to_know_about_INTIMASIA=models.ManyToManyField(HowDidYouGetToKnowAboutINTIMASIA,null=True,blank=True)
    how_did_you_get_to_know_about_INTIMASIA_others=models.TextField(blank=True,null=True)
   
    product_category_interest=models.ManyToManyField(ProductCatogory,null=True,blank=True, related_name='product_category_interest')
    product_category_interest_others=models.TextField(blank=True,null=True)
    product_sub_category_interest=models.ManyToManyField(ProductSubCatogory,null=True,blank=True,related_name='product_sub_category_interest')
    product_sub_category_interest_others=models.TextField(blank=True,null=True)
    subscribe_to_inner_secrets = models.CharField(choices=SUBSCRIBE_TO_INNER_SECRETS,null=True,blank=True, max_length=128)
    is_first_time_to_intimasia = models.CharField(choices=IS_FIRST_TIME_TO_INTIMASIA,null=True,blank=True, max_length=128)

    def save(self, *args, **kwargs):
        if self._state.adding:
            print("adding new Visitor")
            email=self.email 
            password = customUserManager().make_random_password()
        
            print("this is password gfdgdfgdfgfdgffffffffffffffffffffffffffffffffffffffffffffff", password)
            registration_id=unique_id()
            user = User.objects.create_visitor(
                    email=email, password=password,registration_id=registration_id)
            print("lksdfjldsk1----")
           

            self.user = user

            print(user.registration_id)
            print("lksdfjldsk2--")
            context={'email':self.email , 'fname':self.first_name, 'registration_id':user.registration_id ,'lname':self.last_name,'cc':self.cc_email}
            super().save(*args, **kwargs)
            visitor_welcome_mail(email=email, context=context)
            
           
       



class Vender(models.Model):
    
    companyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pinCode = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True,null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    
    briefProfile = models.TextField(max_length=400, blank=True, null=True)
    product_and_services_offer=models.ManyToManyField(VenderProductAndService)

    def __str__(self):
        return self.companyName

class VenderContact(models.Model):
    PERSON_TYPE = (
        (1, "Key Person"),
        (2, "Owner"), 
    )
  

    # designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    designation = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    Vender = models.ForeignKey(Vender, on_delete=models.CASCADE,related_name="vender_contact")
    type = models.IntegerField(choices=PERSON_TYPE,)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    mobile = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)








