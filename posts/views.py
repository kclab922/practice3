from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'detail.html', context)


def create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', id=post.id)

    else:
        form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'form.html', context)


def comment_create(request, post_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post_id = post_id
        comment.save()
        return redirect('posts:detail', id=post_id)


def comment_delete(request, post_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('posts:detail', id=post_id)