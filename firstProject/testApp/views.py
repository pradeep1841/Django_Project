from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    s=Hello Welcome to Django classes..Django is Nursery level concept
    return HttpResponse(s)
