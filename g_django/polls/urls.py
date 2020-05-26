'''
Created on 26 May 2020

@author: yasuhiro
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]