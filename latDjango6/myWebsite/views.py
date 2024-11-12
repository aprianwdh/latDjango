from django.shortcuts import render

def index(request):
    contex = {
        'title':'Home',
        'pembuat':'Django Project',
    }
    return render(request,"index.html",contex)