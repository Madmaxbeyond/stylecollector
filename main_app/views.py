from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Styles:
    def __init__(self, title, brand, description, era):
        self.title = title
        self.brand = brand
        self.description = description
        self.era = era

styles = [
    Styles('Favorite Boots', 'Chanel', 'Black patent', 1960),
    Styles('Houndstooth Coat', 'Vintage', 'Wool', 1950),
    Styles('Mesh Top', 'Other Stories', 'Recycled Poly', 2020)
]        

# Define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def styles_index(request):
    return render(request, 'styles/index.html', { 'styles': styles })

