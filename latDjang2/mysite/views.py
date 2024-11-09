from django.shortcuts import render

def indexHome(request):
    contex = {
        'title':'Website Ter Site',
        'creator':'aprwdh',
        'url':'Home'
    }

    return render(request,"index.html",contex)