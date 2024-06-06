from django.shortcuts import render,redirect
from .models import Stories,Category,Tag,Comment
from django.db.models import Count
from .forms import CommentForm,SearchForm

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

def create_story(request):
    return render(request, 'create_story.html')

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