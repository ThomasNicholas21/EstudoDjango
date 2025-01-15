from . import views
from django.urls import path


app_name = 'blog'


urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('roadmap/', views.road_map, name='roadmap')
]
