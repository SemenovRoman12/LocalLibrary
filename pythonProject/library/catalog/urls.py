from django.urls import path, re_path
from .views import index, BookListView, BookDetailView, LoanedBooksByUserListView, renew_book_librarian, AuthorDelete, \
    AuthorUpdate, AuthorCreate

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', renew_book_librarian, name='renew-book-librarian'),
    re_path(r'^author/create/$', AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', AuthorDelete.as_view(), name='author_delete'),
]

