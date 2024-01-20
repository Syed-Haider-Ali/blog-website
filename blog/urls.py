from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create/blog', create_blog, name='create_blog'),
    path('', list_blog, name='list_blog'),
    path('blog/<int:pk>', blog_detail, name='blog_detail'),
    path('comment/blog/<int:pk>', comment_blog, name='comment_blog')
]
