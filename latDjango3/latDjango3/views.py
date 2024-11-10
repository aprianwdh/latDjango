from django.shortcuts import render

def index(request):
    contex = {
        "judul":"Home",
        'pembuat':'WebKing',
        'nav':{
            '/':'Home',
            '/blog/':'Blog',
        }
    }
    return render(request,"index.html",contex)