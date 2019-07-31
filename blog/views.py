from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import Blog


# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs' : blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    blog.image = request.FILES.get('blog_image')
    blog.save()

    return redirect('home')


def read(request):
    blogs = Blog.objects.all()
    selected_blog = random.sample(list(blogs),1)
    return render(request,'read.html',{"selected_blog" : selected_blog[0]})


def introduce(request):
    return render(request, 'introduce.html')


