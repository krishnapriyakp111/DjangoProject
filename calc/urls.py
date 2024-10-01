from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('contact', views.contact, name='contact'),
    path('blog-post-1', views.blog_post_1, name='blog-post-1'),
    path('blog-post-2', views.blog_post_2, name='blog-post-2'),
    path('blog-post-3', views.blog_post_3, name='blog-post-3'),
]