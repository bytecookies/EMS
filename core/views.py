from django.http import request
from django.db.models import OuterRef, Subquery, Prefetch
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from . import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from core.utility import UserUtility
# Create your views here.


@login_required(login_url="/login")
def index(request):
    firstLogin = False
    print(request.user.id)
    if (request.user.t_n_d == False):
        firstLogin = True
        UserUtility.accept_tnd(request.user.id)

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
            
            print(request.POST.get('finish'),'dslkjflksdjflksdjflkdsjfjldsjlkfjdsjljfljds')
            print(request.POST.get('save_and_edit'),'dslkjflksdjflksdjflkdsjfjldsjlkfjdsjljfljds')
            if request.POST.get('finish') == "submit":
                User.objects.filter(pk=request.user.id).update(participation_form=True)
            return redirect('participation_form')
        # return render(request, 'pages/ExhibitorPages/Forms/participatin_form.html',  {'form': form})

    else:
    
        if request.user.participation_form:
            form=forms.ExhibitorFormDisabled(instance = exhibitor)
            disable_form=0
        else:
            form=forms.ExhibitorForm(instance = exhibitor)
        
    return render(request, 'pages/ExhibitorPages/Forms/participatin_form.html',  {'form': form, "status": disable_form})


@login_required(login_url="/login")
def test(request):
    exhibitor = Exhibitor.objects.filter(pk=request.user).first()
  

    if request.method == 'POST':
        form = forms.ExhibitorForm(request.POST, instance=exhibitor)
        if form.is_valid():
            form.save()
            if request.POST.get('finish') == "submit":
                print("form is freez now")
                User.objects.filter(pk=request.user.id).update(
                    participation_form=True)

    else:
        if request.user.participation_form:
            form = forms.ExhibitorFormDisabled(instance=exhibitor)
        else:
            form=forms.ExhibitorForm(instance = exhibitor)
      

    return render(request, 'pages/test.html', {"form": form})


@login_required(login_url="/login")
def stall_aminities(request):
    return render(request, 'pages/ExhibitorPages/general_info/stall_aminities.html')


@login_required(login_url="/login")
def rules_and_regulations(request):
    return render(request, 'pages/ExhibitorPages/general_info/rules_and_regulations.html')


@login_required(login_url="/login")
def show_info(request):
    return render(request, 'pages/ExhibitorPages/general_info/show_information.html')


@login_required(login_url="/login")
def venders(request):
    venders = VenderContact.objects.filter(type=1).select_related()

    return render(request, 'pages/ExhibitorPages/venders/vender.html', {"venders": venders})


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            print('user', user)
            login(request, user)

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
