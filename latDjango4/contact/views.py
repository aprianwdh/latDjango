from django.shortcuts import render

# Create your views here.
# contact views

def index(request):
    contex = {
        'title':'Contact',
        'pembuat':'Web Pemula',
    }
    return render(request,'contact/index.html',contex)
