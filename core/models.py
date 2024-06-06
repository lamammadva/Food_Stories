from django.db import models
from base.basemodel import BaseModel
# Create your models here.

class ContactUs(BaseModel):
    name =models.CharField(verbose_name="name of contact" , max_length=50,help_text="max 50 characters")
    email = models.EmailField(verbose_name="email of contact" )
    subject = models.CharField(verbose_name='subject of contact',max_length=50,help_text="max 50 characters")
    message=models.TextField(verbose_name='message of contact')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    