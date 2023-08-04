from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'sales', views.SaleViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),   
]