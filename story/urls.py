from django.urls import path
from .views import stories, story, CreateStoryView, recipes,blog_search

urlpatterns = [
    path('stories/', stories, name = 'stories'),
    path('story/<int:pk>', story, name = 'story'),
    path('search/', blog_search, name = 'blog_search'),
    path('create_story/', CreateStoryView.as_view(), name = 'create_story'),
    path('recipes/', recipes, name = 'recipes'),
]