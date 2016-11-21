from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, TestForm1
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def test(request):
    sendform = TestForm1(auto_id=False)
    return render(request, 'blog/test.html', {'sendform': sendform})

def test(request):
    if request.method == "POST":
        sendform = TestForm1(request.POST)
        if sendform.is_valid():
            textin = sendform.cleaned_data['textin']
            print textin
            return redirect('test')
    else:
        sendform = TestForm1()
    return render(request, 'blog/test.html', {'sendform': sendform})