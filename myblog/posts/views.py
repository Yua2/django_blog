from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator


def index(request):
    # return HttpResponse("Hello World! このぺージは投稿のインデックスです。")
    
    postQuerySet = Post.objects.order_by('-published')
    paginator = Paginator(postQuerySet, 5) 
    page = request.GET.get('page')
    postQuery = paginator.get_page(page)

    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts, 'postQuery': postQuery})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
