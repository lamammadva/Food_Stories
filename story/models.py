from django.db import models
from base.basemodel import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here

class Tag(BaseModel):
    name=models.CharField(verbose_name="name of tag",max_length=20,help_text="Max 20 characters")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
class Author(BaseModel):
    name=models.CharField(verbose_name="name of author",max_length=20,help_text="Max 20 characters")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Category(BaseModel):
    name = models.CharField(verbose_name="Name of Category",max_length=20,help_text="Max 20 characters")
    image = models.ImageField(verbose_name="Image of Category",upload_to="category_image")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Stories(BaseModel):
    title =models.CharField(verbose_name="title of stories" , max_length=50,help_text="max 50 characters")
    image = models.ImageField(upload_to="stories_img",verbose_name="Image of Stories")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category of the blog',related_name="story_category")
    descriptions = RichTextUploadingField()
    tag=models.ManyToManyField(Tag,related_name="story_tag")
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='story_author')
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"
        
    
class Comment(BaseModel):
    name =models.CharField(verbose_name="Name of Comment",max_length=20,help_text="max 20 character")
    email = models.EmailField(verbose_name="email of comment")
    message = models.TextField(verbose_name="Mesage of comment")
    story = models.ForeignKey(Stories,on_delete=models.CASCADE,related_name="story_comment")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        

