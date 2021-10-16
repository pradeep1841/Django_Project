from django.shortcuts import render
def name_view(request):
    return render(request,'testapp/name.html')

def age_view(request):
    name=request.GET['name']
    response= render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def gf_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response= render(request,'testapp/gf.html',{'name':name})
    response.set_cookie('age',age)
    return response

def results_view(request):
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    gfname=request.GET['gfname']
    response=render(request,'testapp/results.html',{'name':name,'age':age,'gfname':gfname})
    response.set_cookie('gfname',gfname)
    return response
