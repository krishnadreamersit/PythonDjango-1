from django.contrib import admin
from django.urls import path, include

from app7_1 import  views

urlpatterns = [
    path('', views.index),
]
