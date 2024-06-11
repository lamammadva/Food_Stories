from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django import forms
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","first_name","last_name")

class LofinForm(AuthenticationForm):
    username = forms.EmailInput()
    password = forms.PasswordInput()

    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)