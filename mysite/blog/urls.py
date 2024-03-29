from django.urls import path
from django.urls import include
from django.views.generic import ListView, DetailView
from blog.models import Post


#<pk>  p standard for pimary key


urlpatterns = [ 
                path(r'', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
                path('<int:pk>', DetailView.as_view(model=Post,
                                                         template_name='blog/post.html')),
                
                
            ]


#path(r'(?P<pk>\d+)', DetailView.as_view(model=Post,template_name='blog/post.html')),
