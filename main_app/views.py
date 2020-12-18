from django.shortcuts import render
from .models import Style

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