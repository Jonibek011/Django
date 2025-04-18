from django.urls import path
from .views import ArticleListView, CreateArticleView, ArticleDetail, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('new/', CreateArticleView.as_view(), name='article_new'),
    path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete')
]
