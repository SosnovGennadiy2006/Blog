from django.contrib.auth import forms 
from django.shortcuts import render
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from .forms import SignUpForm, ProfileChangeForm, AvatarChangeForm
from django.template import RequestContext
from json import dumps
import os
from django.conf import settings

def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        return render(request,'500.html')

def home(request):
    return render(request, 'home.html')

def signIn(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/home/')
                else:
                    print('!!!')
                    form.add_error('username', 'A user with this username was not found!')
            else:
                print(form.errors)
        else:
            form = AuthenticationForm()
        return render(request,'signin.html',{'form':form})
    else:
        return HttpResponseRedirect('/home/')

def signUp(request): 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/home/')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def index(rquest):
    return HttpResponseRedirect('/home/')

def profile(request):
    isShow = False
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signIn/')
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST, instance=request.user.profile,
            initial={'first_name': request.user.profile.first_name, 
                     'last_name': request.user.profile.last_name})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
        else:
            isShow = True
    else:
        form = ProfileChangeForm(initial={'first_name': request.user.profile.first_name, 
                     'last_name': request.user.profile.last_name})
    dataJSON = dumps({'show': isShow})
    return render(request, 'profile.html', {'form': form, 'data': dataJSON})

def updateAvatar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signIn/')
    if request.method == 'POST':
        form = AvatarChangeForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save(request.user.profile)
            return HttpResponseRedirect('/profile/')
    else:
        form = AvatarChangeForm()
    return render(request, 'updateAvatar.html', {'form': form})
