from django.urls import path
from .views import stories, CreateStoryView, RecipesView,SearchView,RecipesDetail

urlpatterns = [
    path('stories/', stories, name = 'stories'),
    # path('story/<int:pk>', story, name = 'story'),
    path('search/', SearchView.as_view(), name = 'blog_search'),
    path('create_story/', CreateStoryView.as_view(), name = 'create_story'),
    # path('create_recipe/', CreateRecipeView.as_view(), name = 'create_recipe'),
    path('recipes/', RecipesView.as_view(), name = 'recipes'),
    path('recipes/<int:pk>', RecipesDetail.as_view(), name = 'recipe'),
]