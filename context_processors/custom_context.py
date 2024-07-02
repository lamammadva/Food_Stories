from story.models import Category
from django.db.models import Count

def category_list(request):
    categories = Category.objects.annotate(count= Count('story_category'),recipe_count=Count('recipe_category'))

    return {'category_list':categories}