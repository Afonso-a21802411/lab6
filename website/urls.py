#  hello/urls.py

from django.shortcuts import render
from . import views
from django.urls import path
app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aqui', views.aqui_page_view, name='aqui'),
    path('acola', views.acola_page_view, name='acola'),

]

