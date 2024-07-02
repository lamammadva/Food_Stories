from django.urls import path
from .views import stories, story, CreateStoryView, RecipesView,blog_search,RecipesDetail

urlpatterns = [
    path('stories/', stories, name = 'stories'),
    path('story/<int:pk>', story, name = 'story'),
    path('search/', blog_search, name = 'blog_search'),
    path('create_story/', CreateStoryView.as_view(), name = 'create_story'),
    path('recipes/', RecipesView.as_view(), name = 'recipes'),
    path('recipes_detail/<int:pk>', RecipesDetail.as_view(), name = 'recipes_detail'),
]