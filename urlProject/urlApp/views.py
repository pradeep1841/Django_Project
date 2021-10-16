from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinfo(request):
    s='<h1> Hyderabad Jobs Information Regarding Java Technology</h1>'
    return HttpResponse(s)

def punejobsinfo(request):
    s='<h1> Pune Jobs Information Regarding Python Technology</h1>'
    return HttpResponse(s)

def mumbaijobsinfo(request):
    s='<h1> Mumbai Jobs Information Regarding DBA Technology</h1>'
    return HttpResponse(s)

def noidajobsinfo(request):
    s='<h1>Noida Jobs Information ML technology</h1>'
    return HttpResponse(s)
