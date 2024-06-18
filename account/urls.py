from django.urls import path
from .views import RegisterView, CustomLoginView,ProfileView, ChangePasswordView, ResetPasswordView, ForgetPasswordView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name = 'profile'),
    path('change_password/', ChangePasswordView.as_view(), name = 'change_password'),
    path('reset_password/<str:uidb64>/<str:token>/', ResetPasswordView.as_view(), name = 'reset_password'),
    path('forget_password/', ForgetPasswordView.as_view(), name = 'forget_password')
]