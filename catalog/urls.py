
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('my_books/', views.LoanedBooksByUserListView.as_view(), name='my_books'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('author_detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
    path('my_books/', views.LoanedBooksByUserListView.as_view(), name='my_books'),
    path('book/<uuid:pk>/loan/', views.loan_book_librarian, name='loan_book_librarian'),
    path('available/', views.AvailBooksListView.as_view(), name='all_available'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'), #add book
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),#update book
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'), #delete book

]

