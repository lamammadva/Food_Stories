from django.contrib.auth.forms import AuthenticationForm
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetConfirmView,PasswordChangeView
from .forms import LoginForm
from django.contrib import messages

class RegisterView(CreateView):
    template_name = "register.html"
    model = CustomUser
    form_class = CustomUserCreationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name= "login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        profile = CustomUser.objects.get(email=form.cleaned_data['username']).pk
        return redirect('profile',pk=profile)
 



class ForgetPasswordView(PasswordResetView):
    email_template_name="password_reset_email.html"
    template_name = "forget_password.html"
    success_url = reverse_lazy("login")

    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(ForgetPasswordView, self).get_success_url()
    
   
class ResetPasswordView(PasswordResetConfirmView):
    template_name = "reset_password.html"
    success_url = reverse_lazy("login")
    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(ForgetPasswordView, self).get_success_url()


class ChangePasswordView(PasswordChangeView):
    template_name = "change_password.html"
    success_url = reverse_lazy("login")

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(ChangePasswordView, self).get_success_url()

class ProfileView(DetailView):
    template_name = "user-profile.html"
    model = CustomUser
    context_object_name = "user"
    






# def profile(request):
#     return render(request, 'user-profile.html')

# def change_password(request):
#     return render(request, 'change_password.html')

# def reset_password(request):
#     return render(request, 'reset_password.html')

# def forget_password(request):
#     return render(request, 'forget_password.html')