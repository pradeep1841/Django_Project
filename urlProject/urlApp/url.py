# from django.contrib import admin import url
from django.urls import path
from urlApp import views

urlpatterns = [
    path('hydjobs/', views.hydjobsinfo),
    path('punejobs/', views.punejobsinfo),
    path('mumbaijobs/', views.mumbaijobsinfo),
    path('noidajobs/', views.noidajobsinfo),
]
