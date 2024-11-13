from django.shortcuts import render

def index(request):
    contex = {
        'title':'Home',
        "pembuat":'Django Project',
        'banner':'images/HOMEPAGE.png',
        'css_app':'css/style.css'
    }
    return render(request,'index.html',contex)