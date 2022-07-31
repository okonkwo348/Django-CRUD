from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from . models import Post

class PostListView(ListView):
    model=Post
    template_name="Post_list.py"

class PostCreateView(CreateView):
    model=Post
    fields="_all_"
    template_name="base.html"
    success_url= reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model=Post
    template_name="Post_detail.html"

class PostUpdateView(UpdateView):
    model=Post
    template_name="Post_form.html"
    success_url=reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model=Post
    template_name="Post_delete.html"
    success_url= reverse_lazy("blog:all")