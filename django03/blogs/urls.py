from django.urls import path
from .views import blogPostView

urlpatterns = [
    path('', blogPostView.as_view(), name='home')
]
