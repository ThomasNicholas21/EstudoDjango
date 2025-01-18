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

def post_view(request, post_id):
    print('post', id)
    found_id = None

    for post in posts:
        if post['id'] == post_id:
            found_id = post
            break

    context = {
    'variavel': 'artigos',
    'title': found_id['title'],
    'post': found_id,
    }

    return render(request, 'blog/post.html', context)

def road_map(request):
    context = {
        'variavel': 'Isso é uma variável utilizando a função render',
        'title': 'RoadMap'
    }
    return render(request, 'blog/roadmap.html', context)
