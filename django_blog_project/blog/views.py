from django.shortcuts import render
# Importing http response
from django.http import HttpResponse

from .models import Post

posts = Post.objects.all()


# Create your views here.


def home(request):
    # lets create dictionary
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home Page</h1>')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    # return HttpResponse('<h1>Blog About Page</h1>')
