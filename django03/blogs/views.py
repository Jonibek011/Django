from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class blogPostView(ListView):
    model = Post
    template_name = 'home.html'

class blogPostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class blogPostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']

class blogPostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'author', 'body']

class blogPostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')