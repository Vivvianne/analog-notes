from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Mynotes/home.html', context)


class PostListView(ListView):
    model = Post

def about(request):
    return render(request, 'Mynotes/about.html', {'title': 'About'})

