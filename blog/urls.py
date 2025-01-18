from . import views
from django.urls import path


app_name = 'blog'

# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/

urlpatterns = [
    path('<int:post_id>/', views.post_view, name='post'),
    path('roadmap/', views.road_map, name='roadmap'),
    path('', views.blog_view, name='blog')
]
