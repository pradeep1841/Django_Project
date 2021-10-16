from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
# Create your views here.
def empview(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',context=my_dict)

def index(request):
    return render(request, 'testapp/index.html')    
