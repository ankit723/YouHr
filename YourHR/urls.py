from django.contrib import admin
from django.urls import path, include
from YourHR import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('create', views.createuser, name='create'),
    path('jobs', views.jobs, name='jobs'),
    path('aboutyou', views.aboutyou, name='aboutyou'),
]

if settings.DEBUG:
    urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
