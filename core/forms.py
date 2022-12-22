from django import forms
from django.forms import ModelForm
from .models import *
from utility.models import *
from django.forms import modelformset_factory
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
class ExhibitorForm(ModelForm):
    # Company Details

    companyName=forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    
                }
            ) 
            )
    
    address1 = forms.CharField(required=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "2",
                }
            ) 
            )
    
    address2 = forms.CharField(required=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "2",
                }
            ) 
            )

    zip = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    city = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    state = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    country = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    
    website = forms.URLField(required=False,
            widget=forms.URLInput(
                attrs={
                    "class": "form-control",
                    "pattern":"[Hh][Tt][Tt][Pp][Ss]?:\/\/(?:(?:[a-zA-Z\u00a1-\uffff0-9]+-?)*[a-zA-Z\u00a1-\uffff0-9]+)(?:\.(?:[a-zA-Z\u00a1-\uffff0-9]+-?)*[a-zA-Z\u00a1-\uffff0-9]+)*(?:\.(?:[a-zA-Z\u00a1-\uffff]{2,}))(?::\d{2,5})?(?:\/[^\s]*)?"
                }
            ) 
            )
    company_email = forms.EmailField(required=True,
                             widget=forms.EmailInput(
                                 attrs={
                                     "class": "form-control",
                                 }
                             )
                             )
    # Company Billing Details

    billing_companyName = forms.CharField(required=True,
                                          widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    
    billing_address1 = forms.CharField(required=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows":"2",
                }
            ) 
            )
    billing_address2 = forms.CharField(required=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "2",
                }
            ) 
            )

    billing_zip = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    billing_city = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    billing_state = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    billing_country = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    company_GST = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    company_PAN = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    
    # Key contact person
    contact_person_first_name = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )
    contact_person_last_name = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )

    designation = forms.CharField(required=True,
                                   widget=forms.TextInput(
                                       attrs={
                                           "class": "form-control",
                                       }
                                   )
                                   )
    # designation = forms.ModelChoiceField(required=True,
    #                                      queryset=Designation.objects.all().order_by('name'),

    #                                             widget=forms.Select(
    #                                                 attrs={
    #                                                     "class": "js-example-basic-single form-control",
    #                                                 }
    #                                             )
    #                                             )
    department = forms.ModelChoiceField(required=True,
                                        queryset=Department.objects.all().order_by('name'),
                                                widget=forms.Select(
                                                    attrs={
                                                        "class": "js-example-basic-single form-control",
                                                    }
                                                )
                                                )
    
    # phone = forms.CharField(required=True,
    #                                            widget=forms.TextInput(
    #                                                attrs={
    #                                                    "class": "form-control",
    #                                                }
    #                                            )
    #                                            )
    phone = PhoneNumberField(required=True,
                             widget=PhoneNumberPrefixWidget(initial="IN", 
                                                   attrs={
                                                       "class": "form-control kk",
                                                   }
                                               )
                                               )

    email = forms.EmailField(required=True,
                                               widget=forms.EmailInput(
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )
    # Senior contact person
    senior_person_first_name = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )
    senior_person_last_name = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )

    senior_designation = forms.CharField(required=True,
                                         widget=forms.TextInput(
                                             attrs={
                                                 "class": "form-control",
                                             }
                                         )
                                         )
    # senior_designation = forms.ModelChoiceField(required=True,
    #                                             queryset=Designation.objects.all().order_by('name'),

    #                                             widget=forms.Select(
    #                                                 attrs={
    #                                                     "class": "js-example-basic-single form-control",
    #                                                 }
    #                                             )
    #                                             )
    senior_department = forms.ModelChoiceField(required=True,
                                               queryset=Department.objects.all().order_by('name'),
                                                widget=forms.Select(
                                                    attrs={
                                                        "class": "js-example-basic-single form-control",
                                                    }
                                                )
                                                )
    
    senior_phone = PhoneNumberField(required=True,
                                    widget=PhoneNumberPrefixWidget(initial="IN",
                                                                   attrs={
                                                                       "class": "form-control kk",
                                                                   }
                                                                   )
                                    )
    senior_email = forms.EmailField(required=True,
                                               widget=forms.EmailInput(
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )
    
    
    # Booth Details

    BOOTH_TYPE = (
        ("0", ""),
        ("1", "BARE SPACE"),
        ("2", "SHELL SCHEME")
    )

    boothNumber = forms.CharField(required=True, disabled=True,
                                  widget=forms.TextInput(
                                              attrs={
                                                  "class": "form-control",
                                                 
                                              }
                                          )
                                          )
    boothSize = forms.IntegerField(required=True, disabled=True,
                                  widget=forms.NumberInput(
                                              attrs={
                                                  "class": "form-control",
                                                  
                                              }
                                          )
                                          )

    boothType = forms.ChoiceField(required=True, disabled=True,
                                  choices=BOOTH_TYPE,
                                  widget=forms.Select(
                                              attrs={
                                                  "class": "form-control",
                                                  
                                              }
                                          )
                                          )

    # Business Classification Details
    nature_of_bussiness = forms.ModelMultipleChoiceField(required=True,
                                                         queryset=NatureOfBusiness.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    product_catogory = forms.ModelMultipleChoiceField(required=True,
                                                      queryset=ProductCatogory.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    # product_sub_catogory = forms.ModelMultipleChoiceField(required=True,
    #                                                       queryset=ProductSubCatogory.objects.none(),
    #                                                             widget=forms.SelectMultiple(
    #                                                                 attrs={
    #                                                                     "class":"js-example-basic-multiple form-control"
    #                                                                 }
    #                                                             )
    #                                             )
    our_brand = forms.ModelMultipleChoiceField(required=False,
                                               queryset=Brand.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )

    class Meta:
        model = Exhibitor
        fields = '__all__'
        exclude = ('user', )


        widgets = {
            'product_sub_catogory': forms.SelectMultiple(attrs={'class': 'js-example-basic-multiple  form-control','required':""}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['product_sub_catogory'].queryset = ProductSubCatogory.objects.none()

            if 'product_catogory' in self.data:
                try:
                    product_id = int(self.data.get('product_catogory'))
                    self.fields['product_sub_catogory'].queryset = ProductSubCatogory.objects.filter(
                        product=product_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['product_sub_catogory'].queryset = self.instance.product_catogory.productsubcatogory_set.order_by('name')


class ExhibitorFormDisabled(ModelForm):
    # Company Details

    companyName=forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    
                }
            ) 
            )
    
    address1 = forms.CharField(required=True, disabled=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    
    address2 = forms.CharField(required=True, disabled=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    zip = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    city = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    state = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    country = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    
    website = forms.URLField(required=True, disabled=True,
            widget=forms.URLInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    company_email = forms.EmailField(required=True, disabled=True,
                             widget=forms.EmailInput(
                                 attrs={
                                     "class": "form-control",
                                 }
                             )
                             )
    # Company Billing Details

    billing_companyName = forms.CharField(required=True, disabled=True,
                                          widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    
    billing_address1 = forms.CharField(required=True, disabled=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    billing_address2 = forms.CharField(required=True, disabled=True,
            widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    billing_zip = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    billing_city = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    billing_state = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )

    billing_country = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    company_GST = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    company_PAN = forms.CharField(required=True, disabled=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    
    # Key contact person
    contact_person_first_name = forms.CharField(required=True, disabled=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )
    contact_person_last_name = forms.CharField(required=True, disabled=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )

    designation = forms.CharField(required=True, disabled=True,
                                  widget=forms.TextInput(
                                      attrs={
                                          "class": "form-control",
                                      }
                                  )
                                  )
    department = forms.ModelChoiceField(required=True, disabled=True,
                                        queryset=Department.objects.all(),
                                        

                                                widget=forms.Select(
                                                    attrs={
                                                        "class": "js-example-basic-single form-control",
                                                    }
                                                )
                                                )
    
    phone = forms.CharField(required=True, disabled=True,
                                               widget=forms.TextInput(
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )
    email = forms.EmailField(required=True, disabled=True,
                                               widget=forms.EmailInput(
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )
    # Senior contact person
    senior_person_first_name = forms.CharField(required=True, disabled=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )
    senior_person_last_name = forms.CharField(required=True, disabled=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                    }
                                                )
                                                )

    senior_designation = forms.CharField(required=True, disabled=True,
                                         widget=forms.TextInput(
                                             attrs={
                                                 "class": "form-control",
                                             }
                                         )
                                         )
    senior_department = forms.ModelChoiceField(required=True, disabled=True,
                                        queryset=Department.objects.all(),
                                            #    queryset=None,

                                                widget=forms.Select(
                                                    attrs={
                                                        "class": "js-example-basic-single form-control",
                                                    }
                                                )
                                                )
    
    senior_phone = forms.CharField(required=True, disabled=True,
                                               widget=forms.TextInput(
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )
    senior_email = forms.EmailField(required=True, disabled=True,
                                               widget=forms.EmailInput(
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )
    
    
    # Booth Details

    BOOTH_TYPE = (
        ("0", ""),
        ("1", "BARE SPACE"),
        ("2", "SHELL SCHEME")
    )

    boothNumber = forms.CharField(required=True, disabled=True,
                                  widget=forms.TextInput(
                                              attrs={
                                                  "class": "form-control",
                                                 
                                              }
                                          )
                                          )
    boothSize = forms.IntegerField(required=True, disabled=True,
                                  widget=forms.NumberInput(
                                              attrs={
                                                  "class": "form-control",
                                                  
                                              }
                                          )
                                          )

    boothType = forms.ChoiceField(required=True, disabled=True,
                                  choices=BOOTH_TYPE,
                                  widget=forms.Select(
                                              attrs={
                                                  "class": "form-control",
                                                  
                                              }
                                          )
                                          )

    # Business Classification Details
    nature_of_bussiness = forms.ModelMultipleChoiceField(required=True, disabled=True,
                                                       queryset=NatureOfBusiness.objects.all(),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    product_catogory = forms.ModelMultipleChoiceField(required=True, disabled=True,
                                                      queryset=ProductCatogory.objects.all(),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    product_sub_catogory = forms.ModelMultipleChoiceField(required=True, disabled=True,
                                                          queryset=ProductSubCatogory.objects.all(),
                                                        
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    our_brand = forms.ModelMultipleChoiceField(required=True, disabled=True,
                                               queryset=Brand.objects.all(),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                              )

    class Meta:
        
        model = Exhibitor
        fields = '__all__'
      
        exclude = ('user', )




# ExhibitorFormSet = modelformset_factory(ExhibitorForm)



# visitors forms

class VisitorForm(ModelForm):

    GENDER_CHOICE=(
    ('','-----'),
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
    )    

    first_name = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"First Name...",
                                                    }
                                                )
                                                )
    last_name = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Last Name...",
                                                    }
                                                )
                                                )
    
                                      
    gender = forms.ChoiceField(required=True,choices=GENDER_CHOICE,widget=forms.Select(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"gender...",
                                                    }
                                                )
                                                )
    nationality = forms.ModelChoiceField(required=True,
                                                 queryset=Nationality.objects.all(),
                                                widget=forms.Select(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Nationalityv...",
                                                    }
                                                )
                                                )
    organization_name = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Organisation...",
                                                    }
                                                )
                                                )
    department = forms.ModelChoiceField(required=True, 
                                        queryset=Department.objects.all(),
                                                widget=forms.Select(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Department...",
                                                    }
                                                )
                                                )
                                        

    job_title = forms.CharField(required=True,
                                                widget=forms.TextInput(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Job Title...",
                                                    }
                                                )
                                                )
    apartment_unit_building_floor_etc = forms.CharField(required=True,
                                                widget=forms.Textarea(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Apartment unit building floor etc...",
                                                        "rows":"2"
                                                    }
                                                )
                                                )
    street_address = forms.CharField(required=True,
                                                widget=forms.Textarea(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Street Address...",
                                                        "rows":"2"
                                                    }
                                                )
                                                )
    zip_code = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    country = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    state = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ) 
            )
    town_city_district = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Town City Districts...",
                }
            ) 
            )
    email = forms.EmailField(required=True,
                                                widget=forms.EmailInput(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"Email...",
                                                    }
                                                )
                                                )
    cc_email = forms.EmailField(required=False,
                                                widget=forms.EmailInput(
                                                    attrs={
                                                        "class": "form-control",
                                                        "placeholder":"CC Email...",
                                                    }
                                                )
                                                )

    mobile = PhoneNumberField(required=True,
                             widget=PhoneNumberPrefixWidget(initial="IN", 
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )
    whatsapp = PhoneNumberField(required=False,
                             widget=PhoneNumberPrefixWidget(initial="IN", 
                                                   attrs={
                                                       "class": "form-control",
                                                   }
                                               )
                                               )

    whatsapp_same_as_mobile_or_no_wp = forms.BooleanField(required=False,
                                            
                             widget=forms.RadioSelect(
                                                     choices=((True,"Same as Mobile"),(False,"Don't use WhatsApp")),
                                                   attrs={
                                                       "class": "form-check-input",
                                                        
                                                   }
                             ),
                            
                            
                             
                                               )

   
    
                                               
    nature_of_business = forms.ModelMultipleChoiceField(required=True,
                                                         queryset=NatureOfBusiness.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    nature_of_business_others = forms.CharField(required=False,
                                                                widget=forms.TextInput(
                                                                    attrs={
                                                                        "class":"form-control d-none",
                                                                        
                                                                    }
                                                                )
                                                )
    product_category = forms.ModelMultipleChoiceField(required=True,
                                                         queryset=ProductCatogory.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    product_category_others = forms.CharField(required=False,
                                                                widget=forms.TextInput(
                                                                    attrs={
                                                                        "class":"form-control d-none",
                                                                        
                                                                    }
                                                                )
                                                )                                                                                            
    product_sub_category = forms.ModelMultipleChoiceField(required=True,
                                                         queryset=ProductSubCatogory.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    product_sub_category_others = forms.CharField(required=False,
                                                                widget=forms.TextInput(
                                                                    attrs={
                                                                        "class":"form-control d-none",
                                                                        
                                                                    }
                                                                )
                                                )                                                                                            
    brand = forms.ModelMultipleChoiceField(required=False,
                                                         queryset=Brand.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    brand_others = forms.CharField(required=False,
                                                                widget=forms.TextInput(
                                                                    attrs={
                                                                        "class":"form-control d-none",
                                                                        
                                                                    }
                                                                )
                                                )                                                                                            
    how_did_you_get_to_know_about_INTIMASIA = forms.ModelMultipleChoiceField(required=True,
                                                         queryset=HowDidYouGetToKnowAboutINTIMASIA.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )  

    how_did_you_get_to_know_about_INTIMASIA_others = forms.CharField(required=False,
                                                                widget=forms.TextInput(
                                                                    attrs={
                                                                        "class":"form-control d-none",
                                                                        
                                                                    }
                                                                )
                                                )                                                                                  
    product_category_interest = forms.ModelMultipleChoiceField(required=True,
                                                         queryset=ProductCatogory.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    product_category_interest_others = forms.CharField(required=False,
                                                                widget=forms.TextInput(
                                                                    attrs={
                                                                        "class":"form-control d-none",
                                                                        
                                                                    }
                                                                )
                                                )                                                                
    product_sub_category_interest = forms.ModelMultipleChoiceField(required=True,
                                                         queryset=ProductSubCatogory.objects.all().order_by('name'),
                                                                widget=forms.SelectMultiple(
                                                                    attrs={
                                                                        "class":"js-example-basic-multiple form-control"
                                                                    }
                                                                )
                                                )
    product_sub_category_interest_others = forms.CharField(required=False,
                                                                widget=forms.TextInput(
                                                                    attrs={
                                                                        "class":"form-control d-none",
                                                                        
                                                                    }
                                                                )
                                                )   
              
    SUBSCRIBE_TO_INNER_SECRETS=(
        ('Yes','Yes'),
        ('No','No'),
    )
    IS_FIRST_TIME_TO_INTIMASIA=(
        ('Yes','Yes'),
        ('No','No'),
    )
    
    subscribe_to_inner_secrets = forms.ChoiceField(choices=SUBSCRIBE_TO_INNER_SECRETS, widget=forms.RadioSelect(attrs={
                                                                        "class":"form-check-input"
                                                                    }))

    is_first_time_to_intimasia = forms.ChoiceField(choices=IS_FIRST_TIME_TO_INTIMASIA, widget=forms.RadioSelect(attrs={
                                                                        "class":"form-check-input"
                                                                    }))
                                                  
    # Badge Details
    badge_name = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control mb-4",
                     "placeholder":"Badge Name",
                    "maxlength":"28",

                }
            ) 
            )
    badge_job_title = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control mb-4",
                    "placeholder":"Badge Job Title",
                    "maxlength":"28"
                }
            ) 
            )
    badge_company = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                   "placeholder":"Badge Company",
                    "maxlength":"28"
                }
            ) 
            )
                                                         
    class Meta:
         model = Visitor
         fields = '__all__'
         exclude = ['user','type','password']

