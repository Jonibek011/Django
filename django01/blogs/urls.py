from django.urls import path
from .views import blogListView, blogDetailView, blogCreateView, blogUpdateVIew, blogDeleteView

urlpatterns = [
    path('post/delete/<int:pk>', blogDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>', blogUpdateVIew.as_view(), name='post_update'),
    path('post/new', blogCreateView.as_view(), name='post_create'),
    path('', blogListView.as_view(), name='home'),
    path('post/<int:pk>', blogDetailView.as_view(), name='post_detail' )
]
