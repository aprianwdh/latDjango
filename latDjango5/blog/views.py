from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'title':'Blog',
        'pembuat':'Web Pemula',
    }
    return render(request,'blog/index.html',contex)