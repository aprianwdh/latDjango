from django.shortcuts import render

# Create your views here.
# blog

def index(request):
    contex = {
        'title':'Blog',
        'pembuat':'Web Pemula'
    }
    return render(request,'blog/index.html',contex)

def shop(request):
    contex = {
        'title':'Shop',
        'pembuat':'Web Pemula'
    }
    return render(request,'blog/index.html',contex)

def news(request):
    contex = {
        'title':'News',
        'pembuat':'Web Pemula'
    }
    return render(request,'blog/index.html',contex)