from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from blog.models import Post, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Class tabanlı views


class BlogPageView(ListView):
    # paginations
    paginate_by = 2
    model = Post
    template_name = 'articles.html'


# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'post.html'


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
