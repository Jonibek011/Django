from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class CreateArticleView(CreateView):
    model = Article
    fields = ['title', 'summary', 'body', 'photo', 'author']
    template_name = 'article_new.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'