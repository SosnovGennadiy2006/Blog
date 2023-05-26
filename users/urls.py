from django.urls import path
from . import views 

urlpatterns = [
    path('signUp/', views.signUp),
    path('', views.index),
    path('signIn/', views.signIn),
    path('logout/', views.user_logout),
    path('profile/', views.profile),
    path('profile_<int:user_id>/', views.profileById),
    path('updateAvatar/', views.updateAvatar),
]