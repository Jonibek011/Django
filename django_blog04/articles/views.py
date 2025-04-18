from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'summary', 'body', 'photo', 'author']


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    fields = ('title', 'summary', 'body', 'photo')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
