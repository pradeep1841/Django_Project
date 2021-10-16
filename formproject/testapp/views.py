from django.shortcuts import render
from . import forms     # . ('.' means current working directory)is used for already in testapp forms.py is also in same directory.
# Create your views here.
def studentregisterview(request):
    form=forms.StudentRegisration()
    return render(request, 'testapp/register.html',{'form':form})
