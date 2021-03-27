from django.conf.urls import url
from django.urls import path
import calculations.views as views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('ajaxhandling/', views.ajaxHandling, name='ajaxhandling'),
    path('', views.calculations, name='calculations')
]
