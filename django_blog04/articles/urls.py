from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from django.urls import path


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete')
]
