from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        "judul":"Blog",
        'pembuat':'WebKing',
        'nav':{
            '/':'Home',
            '/blog/':'Blog',
        }
    }
    return render(request,"index.html",contex)