from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'title':'Contact',
        'pembuat':'Django Project',
        'css_app':'about/css/style.css'
    }
    return render(request,'contact/index.html',contex)
