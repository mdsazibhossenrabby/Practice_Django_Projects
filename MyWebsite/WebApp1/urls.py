from django.urls import path
from . import views

app_name = 'WebApp1'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dynamic/<str:page_slug>/', views.dynamic_page, name='dynamic'),
    
]
