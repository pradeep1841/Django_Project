from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'newsapp/index.html')

def moviesinfo(request):
    head_msg="Latest Movies Information"
    msg1='Sonali Slowly getting Cured'
    msg2='Salman is going to marry soon'
    msg3='Modi is going to act in some movie'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request, 'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg="Latest Sports Information"
    msg1='Kohli Gave Left & Right to Bradman Records'
    msg2='India Performance in asian Game'
    msg3='First Gold acquired by China '
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request, 'newsapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg="Latest Politics Information"
    msg1='In Telangana Elections will come just in 2 months'
    msg2='Acche Din aa gaya'
    msg3='Kerala Money gaya...Center Wont accept and wont Give'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request, 'newsapp/news.html',context=my_dict)
