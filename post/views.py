from django.shortcuts import render, get_object_or_404
from .models import Post


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'parts/detail.html', {'post': post})
