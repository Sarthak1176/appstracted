from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('expertise/', views.expertise, name='expertise'),
    path('contact/', views.contact, name='contact'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
]