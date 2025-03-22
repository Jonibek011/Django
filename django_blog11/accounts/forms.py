from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomModel


class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm):
        fields = ['username', 'first_name', 'last_name', 'email', 'age']

class CustomUserChange(UserChangeForm):
    class Meta:
        fields = ['username', 'email', 'age']