from .models import CustomModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomModel
        fields = ['username', 'first_name', 'last_name', 'email', 'age']


class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomModel
        fields = ['username', 'first_name', 'last_name', 'email', 'age']