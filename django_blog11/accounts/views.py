from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomModel
from .forms import CustomUserCreation
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('login')
    model = CustomModel