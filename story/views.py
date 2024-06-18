from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Stories,Category,Tag,Comment
from django.db.models import Count
from django.urls import reverse_lazy
from .forms import CommentForm,SearchForm,CreateStory
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def stories(request):
    category_filter = request.GET.get('category')
    if category_filter:
        all_stories = Stories.objects.filter(category__name=category_filter)
    else:
        all_stories = Stories.objects.all()
    context = {
        'all_stories' : all_stories,
    }
    return render(request, 'stories.html',context)

def story(request,pk):
    all_story = Stories.objects.get(pk=pk)
    recent_blog = Stories.objects.order_by("created_at")[:3]
    all_category= Category.objects.annotate(count= Count('story_category'))
    
    all_tags = Tag.objects.all()
    if request.method =="POST":
        form=CommentForm(data=request.POST)
        if form.is_valid():
            storyform = form.save(commit=False)
            storyform.story = all_story
            storyform.save()
            return redirect('story', pk=pk) 
    else:
            form = CommentForm()

    context={
        'all_story' : all_story,
        'recent_blog':recent_blog,
        'all_category':all_category,
        'all_tags':all_tags,
        'form':form,

    }
    return render(request, 'single.html',context)

class CreateStoryView(CreateView):
    template_name = "create_story.html"
    form_class = CreateStory
    model = Stories 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

  




def recipes(request):
    return render(request, 'recipes.html')

def blog_search(request):
    if request.method == "POST":
        form = SearchForm(data=request.POST)
        if form.is_valid():
            search_form = form.cleaned_data['search']
            search_data =  Stories.objects.filter(title__icontains=search_form)
            context ={
                'search_data':search_data,
            }
            return render(request, 'blog_search.html',context)
    return redirect('stories')