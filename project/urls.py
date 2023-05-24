from django.contrib import admin
from django.urls import path, include
import users.views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signUp/', views.signUp),
    path('home/', views.home),
    path('', views.index),
    path('signIn/', views.signIn),
    path('logout/', views.user_logout),
    path('profile/', views.profile),
    path('updateAvatar/', views.updateAvatar),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
handler500 = views.error_500