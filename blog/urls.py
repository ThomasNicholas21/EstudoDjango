from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_view),
    path('roadmap/', views.road_map)
]
