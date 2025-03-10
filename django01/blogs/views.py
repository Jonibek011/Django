from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class blogListView(ListView):
    model = Post
    template_name = 'home.html'


class blogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class blogCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'author', 'body']


class blogUpdateVIew(UpdateView):
    model = Post
    template_name = 'post_upodate.html'
    fields = ['title', 'body']

class blogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
