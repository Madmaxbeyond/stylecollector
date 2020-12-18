from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('styles/', views.styles_index, name='index'),
    path('cats/<int:style_id>/', views.styles_detail, name='detail'),
]