from django.http import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

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
    return render(request, 'pages/ExhibitorPages/Forms/participatin_form.html')


@login_required(login_url="/login")
def stall_aminities(request):
    return render(request, 'pages/ExhibitorPages/stall_aminities.html')


@login_required(login_url="/login")
def rules_and_regulations(request):
    return render(request, 'pages/ExhibitorPages/rules_and_regulations.html')


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
