from typing import Any
from django.shortcuts import render
from .forms import ContactUsForm
from story.models import Stories
from django.db.models import Count
from django.views.generic import TemplateView
from story.models import Stories
class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['stories'] = Stories.objects.annotate(count = Count("story_comment")).order_by('-count')[:3]
        context["recents"] = Stories.objects.order_by("-created_at")[:4]
        
        return context


    
   

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactUsForm(data=request.POST)
    if form.is_valid():
        form.save()
        form = ContactUsForm()
    context ={
        'form':form
    }
    return render(request, 'contact.html',context)
