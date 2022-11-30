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
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from core.utility import utility_func
from django.core.mail import send_mail, EmailMultiAlternatives


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

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
    firstLogin = False
    print(request.user.id)
    if (request.user.t_n_d == False):
        firstLogin = True
        utility_func.accept_tnd(request.user.id)

    return render(request, 'pages/ExhibitorPages/index.html', {"firstLogin": firstLogin})


@login_required(login_url="/login")
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
    send_mail(email="piyushrmishra143@gmail.com",password="slkdfj")
   
    return render(request, 'pages/components/mail/exhibitor_credential.html',{"email":"piyush@sdkf.com","password":'lkdsjfsdlkhf'})


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


@login_required(login_url="/login")
def stall_aminities(request):
    return render(request, 'pages/ExhibitorPages/general_info/stall_aminities.html')


@login_required(login_url="/login")
def move_in_move_out(request):
    return render(request, 'pages/ExhibitorPages/general_info/move_in_move_out.html')


@login_required(login_url="/login")
def rules_and_regulations(request):
    return render(request, 'pages/ExhibitorPages/general_info/rules_and_regulations.html')


@login_required(login_url="/login")
def show_info(request):
    return render(request, 'pages/ExhibitorPages/general_info/show_information.html')


@login_required(login_url="/login")
def key_contacts(request):
    return render(request, 'pages/ExhibitorPages/general_info/key_contact.html')


@login_required(login_url="/login")
def venders(request):
    venders = VenderContact.objects.filter(type=1).select_related()

    return render(request, 'pages/ExhibitorPages/venders/vender.html', {"venders": venders})


def get_product_sub_catagory_ajax(request):
    if request.method == "GET":
        product_id = request.GET.get("product_id")
        product_sub_catagories = ProductSubCatogory.objects.filter(
            product=product_id).all()
    return render(request, 'pages/ExhibitorPages/components/Ajax/product_subcatagories.html', {"product_sub_catagories": product_sub_catagories})


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

            if user.is_superuser or user.is_staff:
                # print("you are admin")
                return HttpResponseRedirect('/admin/')

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
