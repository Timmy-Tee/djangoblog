from django.urls import path
from . import views
from django.utils.text import slugify

urlpatterns = [
     path('', views.index, name='home'),
     path('single_blog/<str:id>/', views.single_blog_post, name='single_blog'),
     path('blog_reply/', views.blogReply, name='blog_reply'),
     path('create_blog/', views.create_blog, name='create_blog'),
     path('handleLikes/<str:id>/', views.handleLikes, name='handleLikes')
     # path('single_blog_reply/<str:arg1>/<int:arg2>/', views.singleBlogReply, name='reply'),
]
