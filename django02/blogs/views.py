from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class blogPostView(ListView):
    model = Post
    template_name = 'home.html'


class blogDetailVIew(DetailView):
    model = Post
    template_name = 'post_detail.html'

class blogCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'author', 'body']

class blogUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title',  'body']

class blogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
