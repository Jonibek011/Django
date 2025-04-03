from django.urls import path
from .views import ArticleView, ArticleCreateView, ArticleDeleteView, ArticleDetail, ArticleUpdateView


urlpatterns = [
    path('', ArticleView.as_view(), name='article_list'),
    path('new/', ArticleCreateView.as_view(), name='article_new' ),
    path('<int:pk>/', ArticleDeleteView.as_view(), name='article_detail'),
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete')
]
