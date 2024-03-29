from django.shortcuts import render
from . import forms
# Create your views here.
def thankyou_view(request):
    return render(request,'testapp/thankyou.html')

def feedback_view(request):
    if request.method=='GET':
        form=forms.FeedBackForm()

    if request.method=="POST":
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and Printing feedback info')
            print('Student Name:', form.cleaned_data['name'])
            print('Student Roll Number :', form.cleaned_data['rollno'])
            print('Student Mail Id:', form.cleaned_data['email'])
            print('Student Feedback:', form.cleaned_data['feedback'])
            #return thankyou_view(request)
            #return render(request,'testapp/thankyou.html',{'name':form.cleaned_data['name']})
            #return render(request,'testapp/feedback.html',{'form':form})
    return render(request,'testapp/feedback.html',{'form':form})
