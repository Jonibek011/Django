from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomModel


class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomModel
        fields = ['username', 'first_name', 'last_name', 'email', 'age']

class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomModel
        fields = ['username', 'first_name', 'last_name', 'email', 'age']