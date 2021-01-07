from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Style, Accessory
from .forms import WearingForm

# Create your views here.
from django.http import HttpResponse


class StyleCreate(LoginRequiredMixin, CreateView):
    model = Style
    fields = ['title', 'brand', 'description', 'era']
    success_url = '/styles/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StyleUpdate(LoginRequiredMixin, UpdateView):
    model = Style
    fields = ['title', 'brand', 'description', 'era']
    

class StyleDelete(LoginRequiredMixin, DeleteView):
    model = Style
    success_url = '/styles/'       

# Define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def styles_index(request):
    styles = Style.objects.filter(user=request.user)
    return render(request, 'styles/index.html', { 'styles': styles })

@login_required
def styles_detail(request, style_id):
    style = Style.objects.get(id=style_id)
    # instantiate FeedingForm to be rendered in the template
    wearing_form = WearingForm()
    accessories_style_doesnt_have = Accessory.objects.exclude(id__in=style.accessories.all().values_list('id'))
    return render(request, 'styles/detail.html', {
        # pass the style and wearing_form as context
        'style': style, 'wearing_form': wearing_form,
        'accessories': accessories_style_doesnt_have 
    }) 

@login_required
def add_wearing(request, style_id):
    form = WearingForm(request.POST)
    if form.is_valid():
        new_wearing = form.save(commit=False)
        new_wearing.style_id = style_id
        new_wearing.save()
    return redirect('detail', style_id=style_id)

@login_required
def assoc_accessory(request, style_id, accessory_id):
    Style.objects.get(id=style_id).accessories.add(accessory_id)
    return redirect('detail', style_id=style_id)

@login_required
def unassoc_accessory(request, style_id, accessory_id):
    Style.objects.get(id=style_id).accessories.remove(accessory_id)
    return redirect('detail', style_id=style_id)    

class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory
   
class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory    

class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = '__all__'
    success_url = '/accessories/'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = ['title', 'brand', 'color']
        

class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = '/accessories/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)    