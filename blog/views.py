from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import Blog, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    print('good')
    return render(request, "blog/index.html")


def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                response = form.save(commit=False)
                response.created_by = request.user
                response.save()
                return redirect('blog_detail', pk=response.id)
            else:
                print('rola')
        else:
            form = BlogForm()

        context = {
            "form":form
        }
        return render(request, "blog/create_blog.html", context)
    else:
        return redirect('login')
    



def list_blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': blogs})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.blog_comments.all()
    comment_form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'post': blog, 'comments':comments ,'comment_form':comment_form})


def comment_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.created_by = request.user
            comment.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

