from django.shortcuts import render

from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ArticleForm
from .models import Article

def home(request):
    object_list = Article.objects.all()  
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
    return render(request,  
	          'home.html',
		  {'page': page,  
		   'articles': articles})

def viewArticle(request, article_id):
    article = None
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404
    return render(request,'blog/articleDetail.html', context={'article' : article})

class AddArticle(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    model = Article
    login_url = '/signUp/'
    template_name = "blog/createArticle.html"

    def get_success_url(self):
        return '/profile/'
    
    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        return super(AddArticle, self).form_valid(form)
