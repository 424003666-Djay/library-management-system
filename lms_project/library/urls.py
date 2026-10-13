
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('borrowers/', views.borrower_list, name='borrower_list'),
    path('borrowing-records/', views.borrowing_record_list, name='borrowing_record_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('borrow/', views.borrow_book, name='borrow_book'), 
    path('return/<int:record_id>/', views.return_book, name='return_book'),
]