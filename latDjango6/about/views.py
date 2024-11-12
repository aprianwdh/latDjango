from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'title':'About',
        'pembuat':'Django Project',
        'app_css':'about/css/style.css',
    }
    return render(request,'about/index.html',contex)
