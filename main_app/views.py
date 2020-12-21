from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Style
from .forms import WearingForm

# Create your views here.
from django.http import HttpResponse

       

# Define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def styles_index(request):
    styles = Style.objects.all()
    return render(request, 'styles/index.html', { 'styles': styles })

def styles_detail(request, style_id):
    style = Style.objects.get(id=style_id)
    return render(request, 'styles/detail.html', { 'style': style })

class StyleCreate(CreateView):
    model = Style
    fields = '__all__'
    success_url = '/styles/'

class StyleUpdate(UpdateView):
    model = Style
    fields = ['title', 'brand', 'description']

class StyleDelete(DeleteView):
    model = Style
    success_url = '/styles/'    

def add_wearing(request, style_id):
    form = WearingForm(request.POST)
    if form.is_valid():
        new_wearing = form.save(commit=False)
        new_wearing.style_id = style_id
        new_wearing.save()
    return redirect('detail', style_id=style_id)
    
        
