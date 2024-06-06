from django.forms import ModelForm,Form
from .models import Comment
from django import forms
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields = ["name","email","message"]
        widgets = {
            "name":forms.TextInput(attrs={'placeholder':"Name",'class':"form-control"}),
            'email':forms.EmailInput(attrs={'placeholder':"Email address","class":"form-control"}),
            'message':forms.Textarea(attrs={'placeholder':"Message","class":"form-control"})
        }


class SearchForm(forms.Form):
    search =forms.CharField(required=True)