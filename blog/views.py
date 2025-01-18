from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.data import posts
from typing import Any

# Create your views here.
def blog_view(request: HttpRequest) -> HttpResponse:
    context = {
        'variavel': 'artigos',
        'title': 'Blog',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def post_view(request: HttpRequest, post_id: int) -> HttpResponse:
    print('post', id)
    found_id: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_id = post
            break
    
    if found_id is None:
        raise Exception('ID inexistente.')
    
    context = {
    'variavel': 'artigos',
    'title': found_id['title'],
    'post': found_id,
    }
    
    return render(request, 'blog/post.html', context)

def road_map(request: HttpRequest) -> HttpResponse:
    context = {
        'variavel': 'Isso é uma variável utilizando a função render',
        'title': 'RoadMap'
    }

    return render(request, 'blog/roadmap.html', context)
