from django.contrib import admin
from .models import Stories,Category,Tag,Comment,Author,Recipes
from django.utils.html import format_html
# Register your models here.

class StoriesAdmin(admin.ModelAdmin):
    list_display = ("title","getImage","descriptions",'author')


    def getImage(self,obj):
        if obj.image:
            url = '<img src="{url}" width="200px" height="200px"/>'.format(url=obj.image.url)
            return format_html(url)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","getImage")


    def getImage(self,obj):
        if obj.image:
            url = '<img src="{url}" width="200px" height="200px"/>'.format(url=obj.image.url)
            return format_html(url)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ("title","getImage","descriptions",)


    def getImage(self,obj):
        if obj.image:
            url = '<img src="{url}" width="200px" height="200px"/>'.format(url=obj.image.url)
            return format_html(url)
        
admin.site.register(Stories,StoriesAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Recipes,RecipesAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Author)