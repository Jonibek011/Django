from django.urls import path
from .views import blogPostView, blogDetailVIew, blogUpdateView, blogDeleteView, blogCreateView

urlpatterns = [
    path('post/create', blogCreateView.as_view(), name='post_create'),
    path('post/delete/<int:pk>', blogDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>', blogUpdateView.as_view(), name='post_update'),
    path('', blogPostView.as_view(), name= 'home'),
    path('post/<int:pk>', blogDetailVIew.as_view(), name='post_detail' )
]
