from django.shortcuts import render

def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newCount=count+1
    response= render(request,'testapp/count.html',{'count':newCount})
    response.set_cookie('count',newCount,max_age=60)
    return response
