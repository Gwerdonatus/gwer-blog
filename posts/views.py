from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, "posts/posts_list.html", {'posts': posts })


@login_required
def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})

