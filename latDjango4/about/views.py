from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'title':'About',
        'pembuat':'Web Pemula'
    }
    return render(request,"about/index.html",contex)
