from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from .models import Stories,Category,Tag,Comment,CustomUser,Recipes
from django.db.models import Count
from django.urls import reverse_lazy
from .forms import CommentForm,SearchForm,CreateStoryForm
from django.views.generic import CreateView,ListView,DetailView
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
    all_category= Category.objects.annotate(count = Count('story_category'))
    all_tags = Tag.objects.all()
    recent_blog = Stories.objects.order_by("created_at")[:3]
    

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
    form_class = CreateStoryForm
    model = Stories 
    def get_context_data(self, **kwargs):
        context = super(CreateStoryView,self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return  context
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

  




class RecipesView(ListView):
    template_name = "recipes.html"
    model = Recipes
    context_object_name = "recipes"
    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Recipes.objects.filter(category__name = category).all()
        return Recipes.objects.all()
       


class RecipesDetail(DetailView):
    template_name = "recipes-detail.html"
    model = Recipes
    context_object_name = "recipe"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['recents'] = Recipes.objects.order_by('-created_at')[:3]
        context['tags'] = Tag.objects.all()
        return context
    
   




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