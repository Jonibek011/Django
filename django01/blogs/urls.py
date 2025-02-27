from django.urls import path
from .views import blogListView, blogDetailView

urlpatterns = [
    path('', blogListView.as_view(), name='home'),
    path('post/<int:pk>', blogDetailView.as_view(), name='post_detail' )
]
