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
    path('create_author/', views.AuthorCreateView.as_view(), name='create-author'),
    path('authors', views.AuthorsTableView.as_view()),
    path('api/', include(router.urls)),
    path('deleteauthor/<int:author_id>/', views.delete_author, name='delete-author'),
    path('sales', views.IndexSales.as_view(), name='sales'),
    path('editauthor/<int:author_id>/', views.EditAuthorView.as_view(), name='edit-author'),
    path('detail-author-view/<int:pk>/', views.AuthorDetailView.as_view(), name='detail-author-view'),
    path('book/details/<int:pk>/', views.BookDetailView.as_view(), name='detail-book'),
    path('book/new/<int:author_id>', views.BookCreateView.as_view(), name='create-book'),
    path('book/edit/<int:book_id>', views.EditBookView.as_view(), name='edit-book'),
    path('book/delete/<int:book_id>', views.delete_book, name='delete-book'),
    path('create_sale/<int:book_id>/', views.create_sale, name='create_sale'),
    path('book/<int:book_id>/sales/', views.book_sales_index, name='book_sales_index'),
    path('edit_sale/<int:sale_id>/', views.EditSaleView.as_view(), name='edit_sale'),
    path('deletesale/<int:sale_id>/', views.delete_sale, name='delete-sale'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)