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
    path('book/<int:book_id>/reviews', views.ReviewsView.as_view(), name='reviews'),
    path('create_review/<int:book_id>/', views.create_review, name='create_review'),
    path('edit_review/<int:review_id>/', views.EditReviewView.as_view(), name='edit_review'),
    path('deletereview/<int:review_id>/', views.delete_review, name='delete-review'),
    path('upvote_review/<int:review_id>/', views.upvote_review, name='upvote_review'),
    path('downvote_review/<int:review_id>/', views.downvote_review, name='downvote_review'),
    path('search/', views.search, name='search_books'),
    path('top10Books/', views.TopRatedTableView.as_view(), name='top_10_rated'),
    path('top50Books/', views.TopSellerTableView.as_view(), name='top_50_rated'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)