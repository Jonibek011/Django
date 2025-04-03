from django.shortcuts import render
from django.views.generic import ListView,  DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy
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


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = "article_update.html"



class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')