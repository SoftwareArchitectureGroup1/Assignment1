from django.urls import path, include

from .views import views

urlpatterns = [
    path('', views.home, name='home'),
    
]