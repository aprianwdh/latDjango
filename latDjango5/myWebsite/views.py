from django.shortcuts import render

def index(request):
    contex = {
        'title':'Home',
        'pembuat':'Web Pemula',
    }
    return render(request,'index.html',contex)