from django.urls import path
from .views import ArticleListView, CreateArticleView, ArticleDetail

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('new/', CreateArticleView.as_view(), name='article_new'),
    path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),
]
