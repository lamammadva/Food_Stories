from django.urls import path
from .views import HomeView, about, contact

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact')
]