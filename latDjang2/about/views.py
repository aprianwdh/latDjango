from django.shortcuts import render

# Create your views here.
def indexAbout(request):
    contex = {
        'title':'Website Ter Site',
        'creator':'aprwdh',
        'url':'About'
    }
    return render(request,'about/index.html',contex)
