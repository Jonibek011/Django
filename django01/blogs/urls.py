from django.urls import path
from .views import blogListView, blogDetailView, blogCreateView, blogUpdateVIew

urlpatterns = [
    path('post/edit', blogUpdateVIew.as_view(), 'post_update'),
    path('post/new', blogCreateView.as_view(), name='post_create'),
    path('', blogListView.as_view(), name='home'),
    path('post/<int:pk>', blogDetailView.as_view(), name='post_detail' )
]
