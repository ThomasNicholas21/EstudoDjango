from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/index.html')

def road_map(request):
    return render(request, 'blog/roadmap.html')