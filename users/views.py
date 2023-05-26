from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import Http404, HttpResponseRedirect

from .forms import SignUpForm, ProfileChangeForm, AvatarChangeForm
from json import dumps
from blog.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

def error_404(request, exception):
    data = {}
    return render(request,'404.html', data)

def error_500(request):
    return render(request,'500.html')

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
            form = AuthenticationForm()
        return render(request,'users/signin.html',{'form':form})
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
    return render(request,'users/signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def index(rquest):
    return HttpResponseRedirect('/home/')

def getUserPagination(request, user_id):
    object_list = Article.objects.filter(author_id=user_id)
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:  
        articles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        articles = paginator.page(1)
    except EmptyPage: 
        page = paginator.num_pages
        articles = paginator.page(paginator.num_pages)
    return {'page': page,  
		   'articles': articles}

def profile(request):
    isShow = False
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signIn/')
    p_data = getUserPagination(request, request.user.id)
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
    return render(request, 'users/profile.html', {'form': form, 'data': dataJSON, 'page': p_data['page'],
                                                  'articles': p_data['articles']})

def profileById(request, user_id):
    if request.user.is_authenticated and request.user.id == user_id:
        return HttpResponseRedirect('/profile/')
    user = None
    try:
        user = User.objects.get(id=user_id)
        p_data = getUserPagination(request, user_id)
        return render(request, 'users/profileById.html', {'user': user, 'page': p_data['page'],
                                                  'articles': p_data['articles']})
    except  User.DoesNotExist:
        raise Http404

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
    return render(request, 'users/updateAvatar.html', {'form': form})
