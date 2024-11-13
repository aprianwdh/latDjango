from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'title':'About',
        'pembuat':'django Project',
        'banner':'about/images/ABOUTPAGE.png',
        'css_app':'about/css/style.css',
    }
    return render(request,'about/index.html',contex)
