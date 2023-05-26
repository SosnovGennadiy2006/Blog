from django.urls import path
from .views import AddArticle, viewArticle, home

urlpatterns = [
    path('createArticle/', AddArticle.as_view(), name='createArticle'),
    path('article_<int:article_id>/', viewArticle, name='article_list'),
    path('home/', home, name='home')
]