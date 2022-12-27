from django.http import request
from django.db.models import OuterRef, Subquery, Prefetch
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from utility.models import *
from . import forms
from .models import User
from Exhibitor_utility.models import  ExhibitorDownload, StaticDownload, PromotionalCreative, FloorPlan
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from core.utility import utility_func
from django.core.mail import send_mail, EmailMultiAlternatives
from .decorators import *

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import hashlib
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models import Q

import json
import base64


def getEncodedUrl(fname,lname,registration_id):
    d={"register_id":registration_id,"fname":fname,"lname":lname}
    j=json.dumps(d)
    encoded = base64.b64encode(j.encode('utf-8'))
    return encoded.decode('utf-8')
# Create your views here.


def send_mail(email, password):
   
    htmly = get_template('pages/components/mail/exhibitor_credential.html')

    d = {'email': email, "password": password}

    subject, from_email = 'Your Login Credential', 'Intimasia <no-reply@intimasia.in>'
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(
        subject=subject, from_email=from_email, to=[email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@login_required(login_url="/login")
def index(request):
      if request.user.is_superuser or request.user.is_staff:
                # print("you are admin")
                return HttpResponseRedirect('/admin/')

      if request.user.isExhibitor:
                # print("you are Exhibitor")
                return redirect('exhibitor_dashboard')

      if request.user.isVisitor:
                # print("you are Visitor")
                return redirect('visitor_dashboard')





@exhibitor_required()
def exhibitor_dashboard(request):
    firstLogin = False
    print(request.user.id)
    welcome_message_details=None
    if (request.user.t_n_d == False):
        firstLogin = True
        
        if request.user.isExhibitor:
            try:
                welcome_message_details=Exhibitor.objects.filter(user=request.user.id).get()
            except(Exception):
                welcome_message_details=None

        utility_func.accept_tnd(request.user.id)

    

    return render(request, 'pages/ExhibitorPages/index.html', {"firstLogin": firstLogin,"welcome_details":welcome_message_details})




@exhibitor_required()
def participation_form(request):
    print(request.user)
    exhibitor = Exhibitor.objects.filter(pk=request.user).first()
    print(exhibitor)
    disable_form = 1
    if request.method == 'POST':
        print("this is post")
        form = forms.ExhibitorForm(request.POST, instance=exhibitor)
        if form.is_valid():
            print("form is valid __------------------------------------")
            
            form.save()

            print(request.POST.get('finish'),
                  'dslkjflksdjflksdjflkdsjfjldsjlkfjdsjljfljds')
            print(request.POST.get('save_and_edit'),
                  'dslkjflksdjflksdjflkdsjfjldsjlkfjdsjljfljds')
            if request.POST.get('finish') == "submit":
                User.objects.filter(pk=request.user.id).update(
                    participation_form=True)
            return redirect('participation_form')
        # return render(request, 'pages/ExhibitorPages/Forms/participatin_form.html',  {'form': form})

    else:

        if request.user.participation_form:
            form = forms.ExhibitorFormDisabled(instance=exhibitor)
            disable_form = 0
        else:
            form = forms.ExhibitorForm(instance=exhibitor)

    return render(request, 'pages/ExhibitorPages/Forms/participatin_form.html',  {'form': form, "status": disable_form})


@login_required(login_url="/login")
def test(request):
    context={'barcodes':'IM00932','fname':'Piyush','lname':'Mishra'}
    return render(request, 'pages/components/mail/visitor_welcome.html',context)

@exhibitor_required()
def exhibitor_downloads(request):
   
    exhibitor_download=ExhibitorDownload.objects.filter(exhibitor=request.user.id)
    print(exhibitor_download)
    return render(request, 'pages/ExhibitorPages/downloads/index.html',{'downloads':exhibitor_download})

@exhibitor_required()
def exhibitor_static_downloads(request):
   
    static_download=StaticDownload.objects.all()
    print(static_download)

    return render(request, 'pages/ExhibitorPages/downloads/static_downloads.html',{'downloads':static_download})

@exhibitor_required()
def event_promotion_download(request):
    promotoin_download=PromotionalCreative.objects.filter(exhibitor=request.user.id)
    print(promotoin_download.exists())
    return render(request, 'pages/ExhibitorPages/downloads/event_promotion.html',{'downloads':promotoin_download})

@exhibitor_required()
def floor_plan(request):
    floor_plan=FloorPlan.objects.all()
    # print(promotoin_download)
    return render(request, 'pages/ExhibitorPages/downloads/floor_plan.html',{'downloads':floor_plan})


@exhibitor_required()
def stall_aminities(request):
    return render(request, 'pages/ExhibitorPages/general_info/stall_aminities.html')


@exhibitor_required()
def move_in_move_out(request):
    return render(request, 'pages/ExhibitorPages/general_info/move_in_move_out.html')


@exhibitor_required()
def rules_and_regulations(request):
    return render(request, 'pages/ExhibitorPages/general_info/rules_and_regulations.html')


@exhibitor_required()
def show_info(request):
    return render(request, 'pages/ExhibitorPages/general_info/show_information.html')


@exhibitor_required()
def key_contacts(request):
    return render(request, 'pages/ExhibitorPages/general_info/key_contact.html')


@exhibitor_required()
def venders(request):
    venders = VenderContact.objects.filter(type=1).select_related()

    return render(request, 'pages/ExhibitorPages/venders/vender.html', {"venders": venders})



# visitors view

def visitors_registration(request):

    if request.method == 'POST':
        form = forms.VisitorForm(request.POST)

        if form.is_valid():
            # print(form)
            k=form.save()
            print(k.user.registration_id)
            print(k.first_name)
            print(k.last_name)
            
            url_str=getEncodedUrl(fname=k.first_name,lname=k.last_name,registration_id=k.user.registration_id)

            return redirect(f'https://intimasia.in/visitor_registration_confirmationPage.php?id={url_str}')
    else:
        form = forms.VisitorForm()
    # return render(request,'pages/test.html',{'form':form})
    return render(request,'pages/VisitorPages/auth/registration.html',{'form':form})

@visitor_required()
def visitor_dashboard(request):
    return render(request, 'pages/VisitorPages/index.html')


# @visitor_required()
# def exhibitor_list(request):
#     queryset=Exhibitor.objects.select_related('user','department','senior_department').all()
#     return render(request, 'pages/VisitorPages/exhibitor_views/list.html',{'exhibitors':queryset})


@visitor_required()
def exhibitor_list(request):
    queryset=Exhibitor.objects.select_related('user','department','senior_department').filter(Q(user__participation_form=True)).order_by('companyName').distinct()
    q=request.GET.get('q')
    if q is not None and q!='':
        queryset=Exhibitor.objects.select_related('user','department','senior_department').filter(Q(our_brand__name__icontains=q)| Q(companyName__icontains=q)|Q(boothNumber__icontains=q) & Q(user__participation_form=True)).order_by('companyName').distinct()
        # queryset=Exhibitor.objects.select_related('user','department','senior_department').filter(our_brand)
    paginator=Paginator(queryset,10)    
    page=request.GET.get('page')
    page_exhibitor=paginator.get_page(page)
    print(page_exhibitor.paginator.page_range)
    exhibitor_count=queryset.count()
    # print(exhibitor_count)
    return render(request, 'pages/VisitorPages/exhibitor_views/list.html',{'exhibitors':page_exhibitor})




@visitor_required()
def exhibitor_detail(request,pk):
    queryset=Exhibitor.objects.select_related('user','department','senior_department').get(pk=pk)
    print(queryset.address1)
    print(queryset)
    return render(request, 'pages/VisitorPages/exhibitor_views/detail.html',{'exhibitor':queryset})
 





# utilities

def get_product_sub_catagory_ajax(request):
    if request.method == "GET":
        product_id = request.GET.get("product_id")
        product_sub_catagories = ProductSubCatogory.objects.filter(
            product=product_id).all()
    return render(request, 'pages/ExhibitorPages/components/Ajax/product_subcatagories.html', {"product_sub_catagories": product_sub_catagories})



# auth
@login_required(login_url="/login")
def change_password(request):
    # send_mail(email="piyushrmishra143@gmail.com",password="slkdfj")
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pages/ExhibitorPages/reset-password/reset-password.html', {
        'form': form
    })


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            print('user', user)
            login(request, user)
            request.session.set_expiry(0)
            print(user.is_superuser)

          
            if 'next' in request.POST:
                print("krupa", request.POST.get('next'))
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'pages/ExhibitorPages/login/login.html', {'form': form})


@login_required(login_url="/login")
def logout_view(request):
    if request.user.is_authenticated:
        print('In logout')
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
