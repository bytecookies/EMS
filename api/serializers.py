from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
from core.models import Exhibitor, Visitor, Meeting, EventAgenda

from utility.models import NatureOfBusiness, Brand, ProductCatogory, ProductSubCatogory, Department, Nationality

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField()


class NatureOfBussinessSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=255)

class ProductCatogorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=255)

class ProductSubCatogorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=255)

class OurBrandSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=255)



class ExhibitorDetailSerializer(serializers.ModelSerializer):

    # user=serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all()
    # )
   
    nature_of_business=NatureOfBussinessSerializer(many=True,source='nature_of_bussiness')
    product_category=ProductCatogorySerializer(many=True,source='product_catogory')
    product_sub_category=ProductSubCatogorySerializer(many=True, source='product_sub_catogory')
    our_brand=OurBrandSerializer(many=True)
    company_name = serializers.CharField(max_length=255,source='companyName')
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
        ,source='user')
    booth_number=serializers.CharField(max_length=255, source='boothNumber')
    # nature_of_bussiness=serializers.PrimaryKeyRelatedField(queryset=NatureOfBusiness.objects.select_related('nature_of_bussiness').all(),many=True)
    class Meta:
        model=Exhibitor
        fields=['user_id','company_name','company_description','contact_person_first_name','contact_person_last_name','designation','city','state','country','booth_number','our_brand','nature_of_business','product_category','product_sub_category']
    
class ExhibitorListSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
        ,source='user')
    company_name = serializers.CharField(max_length=255,source='companyName')
    booth_number = serializers.CharField(max_length=255,source='boothNumber')
    class Meta:
        model=Exhibitor
        fields=['user_id','company_name','contact_person_first_name','contact_person_last_name','designation','booth_number']
    
   

class VisitorListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visitor
        fields=['user','first_name','last_name','email']
        read_only_fields=['user']



class VisitorDetailSerializer(serializers.ModelSerializer):
    user_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()
        ,source='user')
    
    registration_id=serializers.CharField(read_only=True,source='user.registration_id')
    
    nationality_id=serializers.PrimaryKeyRelatedField(queryset=Nationality.objects.all()
        ,source='nationality')
    department_id=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all()
        ,source='department')
    
    # nationality_id=serializers.IntegerField(source='nationality.pk')
    # department_id=serializers.IntegerField(source='department.pk')
    
    class Meta:
        model=Visitor
        fields=['user_id','registration_id','first_name','last_name','email','gender','nationality_id','organization_name','department_id','job_title','apartment_unit_building_floor_etc','street_address','zip_code','country','state','town_city_district','email','cc_email','mobile','mobile','whatsapp','whatsapp_same_as_mobile_or_no_wp','nature_of_business','nature_of_business_others','product_category','product_category_others','product_sub_category','product_sub_category_others','brand','brand_others','how_did_you_get_to_know_about_INTIMASIA','how_did_you_get_to_know_about_INTIMASIA_others','product_category_interest','product_category_interest_others','product_sub_category_interest','product_sub_category_interest_others','subscribe_to_inner_secrets','is_first_time_to_intimasia','badge_name','badge_job_title','badge_company']
        
        read_only_fields=['user_id','email']
        
        def create(self, validated_data):
            return Visitor.objects.create(**validated_data)
        




class VisitorCreateSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=255)
    class Meta:
        model=Visitor
        fields=['user','first_name','last_name','email','password']
        read_only_fields=['user']



# meetings


class MeetingSerializer(serializers.ModelSerializer):
    
    
    sender_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()
        ,source='sender')
    
    receiver_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()
        ,source='receiver')
    
    receiver_name=serializers.SerializerMethodField('get_receiver_name')
    

    @classmethod
    def get_receiver_name(self, obj):
        try:
            k=User.objects.prefetch_related('exhibitor').get(pk=obj.receiver_id)
            k=str(k.exhibitor.contact_person_first_name) + " -" + str(k.exhibitor)
        except Exception:
            k=None
        return k
    
    class Meta:
        model=Meeting
        fields=['id','sender_id','receiver_id','receiver_name','sender_type','personal_message','date','time_form','time_to','status']
        read_only=['receiver_name','status']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventAgenda
        fields=['id','topic','speaker','description','date','time_form','time_to']
    



# utilities

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Brand
        fields='__all__'
        
class NatureOfBusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=NatureOfBusiness
        fields='__all__'
        

    
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Department
        fields='__all__'
        
class ProductCatogorySerializer(serializers.ModelSerializer):

    class Meta:
        model=ProductCatogory
        fields='__all__'
        
class ProductSubCatogorySerializer(serializers.ModelSerializer):

    class Meta:
        model=ProductSubCatogory
        fields='__all__'
        
class NationalitySerializer(serializers.ModelSerializer):

    class Meta:
        model=Nationality
        fields='__all__'
        

    