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
    path('styles/<int:style_id>/add_wearing/', views.add_wearing, name='add_wearing'),
    path('styles/<int:style_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update', views.AccessoryUpdate.as_view(), name='accessory_update'),
    path('accessories/<int:pk>/delete', views.AccessoryDelete.as_view(), name='accessory_delete'),      
]