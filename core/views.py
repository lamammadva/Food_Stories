from django.shortcuts import render
from .forms import ContactUsForm
def home(request):
    return render(request, 'index.html')

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
