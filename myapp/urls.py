from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name = 'index'),
    
    path('starter/', views.starter, name = 'starter'),
    
    path('about/', views.about, name = 'about'),
    
    path('chefs/', views.chefs, name = 'chefs'),
    
    path('contact/', views.contact, name = 'contact'),
    
    path('events/', views.events, name = 'events'),
    
    path('menu/', views.menu, name = 'menu'),
    
    path('gallery/', views.gallery, name = 'gallery'),
    
    path('booking/', views.booking, name = 'booking'),
    
]
