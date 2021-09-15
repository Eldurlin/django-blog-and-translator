from blog.models import Post
from django.shortcuts import render
from django.views import generic

# Create your views here.

class BlogView(generic.DeleteView):
    model = Post
    template_name = 'blog.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'
