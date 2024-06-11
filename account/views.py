from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .forms import LofinForm

class RegisterView(CreateView):
    template_name = "register.html"
    model = CustomUser
    form_class = CustomUserCreationForm

class CustomLoginView(LoginView):
    form_class = LofinForm
    template_name= "login.html"

    
    # def dispatch(self, request, *args , **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect("login/")
    #     return super(CustomLoginView,self).dispatch(request, *args, **kwargs)




def profile(request):
    return render(request, 'user-profile.html')

def change_password(request):
    return render(request, 'change_password.html')
    
def reset_password(request):
    return render(request, 'reset_password.html')
    
def forget_password(request):
    return render(request, 'forget_password.html')