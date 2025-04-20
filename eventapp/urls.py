from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('register/', include('userapp.urls')),  # This includes app URLs
]
