from django.shortcuts import render
from django.http import HttpResponse

# Blog views
def indexBlog(request):
    contex = {
        'title':'Website Ter Site',
        'creator':'aprwdh',
        'url':'Blog'
    }
    return render(request,'blog/index.html',contex)

def tierList(request):
    contex = {
        'title':'Website Ter Site',
        'creator':'aprwdh',
        'url':'tier list'
    }
    return render(request,'blog/index.html',contex)
    # return HttpResponse("aoidjeajdoa")

def news(request):
    contex = {
        'title':'Website Ter Site',
        'creator':'aprwdh',
        'url':'News'
    }
    return render(request,'blog/index.html',contex)

def comunity(request):
    contex = {
        'title':'Website Ter Site',
        'creator':'aprwdh',
        'url':'Comunity'
    }
    return render(request,'blog/index.html',contex)