from django.urls import path, include
from django.conf.urls.static import static

from . import views
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'sales', views.SaleViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('indexauthors', views.IndexAuthorsView.as_view(), name='indexAuthor'),
    path('detail/<int:author_id>/', views.detailAuthor, name='detail-author-view'),
    path('create_author/', views.AuthorCreateView.as_view(), name='create-author'),
    path('authors', views.AuthorsTableView.as_view()),
    path('api/', include(router.urls)),
    path('deleteauthor/<int:author_id>/', views.delete_author, name='delete-author'),
    path('editauthor/<int:author_id>/', views.EditAuthorView.as_view(), name='edit-author'),
    path('author/<int:author_id>/', views.AuthorDetailView.as_view(), name='author-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)