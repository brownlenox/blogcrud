from django.shortcuts import render, redirect, get_object_or_404
from . models import Post
from . forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('-created_at', '-created_on')
    return render(request, 'blogsysytem/index.html', {"posts":posts})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = PostForm()
    return render(request, 'blogsysytem/create.html', {"form":form})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogsysytem/detail.html',{"post":post})

def update(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        post.title = title
        post.body = body
        post.save()
        return redirect('detail', pk=post.pk)
    return render(request, 'blogsysytem/update.html',{'post':post})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')
