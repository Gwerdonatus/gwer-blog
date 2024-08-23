from django.urls import path 
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.posts_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail_view, name='post_detail_view'),
    
   
]
