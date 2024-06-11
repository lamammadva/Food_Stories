from django.urls import path
from .views import RegisterView, CustomLoginView,profile, change_password, reset_password, forget_password
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', profile, name = 'profile'),
    path('change_password/', change_password, name = 'change_password'),
    path('reset_password/', reset_password, name = 'reset_password'),
    path('forget_password/', forget_password, name = 'forget_password')
]