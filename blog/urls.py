from . import views
from django.urls import path


app_name = 'blog'


urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('post/<id>', views.post_view, name='post'),
    path('roadmap/', views.road_map, name='roadmap')
]
