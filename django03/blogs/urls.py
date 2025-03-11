from django.urls import path
from .views import blogPostView, blogPostDetail, blogPostUpdate, blogPostCreate, blogPostDelete

urlpatterns = [
    path('post/<int:pk>', blogPostDetail.as_view(), name='post_detail'),
    path('', blogPostView.as_view(), name='home'),
    path('post/edit/<int:pk>', blogPostUpdate.as_view(), name= 'post_update'),
    path('post/new', blogPostCreate.as_view(), name='post_create'),
    path('post/delete/<int:pk>', blogPostDelete.as_view(), name='post_delete')

]
