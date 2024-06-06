from django.forms import  ModelForm  
from .models import ContactUs
from django import forms


class ContactUsForm(ModelForm):
    class Meta:
        model=ContactUs
        fields=['name','email','subject','message']
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control",'placeholder':"Name"}),
            "email":forms.EmailInput(attrs={"class":"form-control",'placeholder':"Email"}),
            "subject":forms.TextInput(attrs={"class":"form-control",'placeholder':"Subject"}),
            "message":forms.Textarea(attrs={"class":"form-control",'placeholder':"Message"}),

        }
       
        
