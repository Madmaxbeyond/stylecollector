from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('styles/', views.styles_index, name='index'),
    path('styles/<int:style_id>/', views.styles_detail, name='detail'),
    path('styles/create/', views.StyleCreate.as_view(), name='styles_create'),
    path('styles/<int:pk>/update/', views.StyleUpdate.as_view(), name='styles_update'),
    path('styles/<int:pk>/delete/', views.StyleDelete.as_view(), name='styles_delete'),
    
]