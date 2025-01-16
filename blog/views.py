from django.shortcuts import render
from blog.data import posts


# Create your views here.
def blog_view(request):
    context = {
        'variavel': 'artigos',
        'title': 'Blog',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def road_map(request):
    context = {
        'variavel': 'Isso é uma variável utilizando a função render',
        'title': 'RoadMap'
    }
    return render(request, 'blog/roadmap.html', context)