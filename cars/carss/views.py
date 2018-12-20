from django.shortcuts import render

from .models import Post

# Create your views here.
def posts_list (request):
    posts = Post.objects.all()
    return render (request, 'cars/index.html', context ={'posts' : posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact= slug)
    return render (request, 'cars/post_detail.html', context = {'post' : post})
