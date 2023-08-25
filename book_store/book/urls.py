from django.urls import path
# from . import views
from book.views import home,store_book,show_books,eidt_book,delete_book

urlpatterns = [
    path('',home),
    path('store_new_book/',store_book,name='storebook'),
    path('show-books/',show_books,name='show_books'),
    path('edit_book/<int:id>',eidt_book,name='edit_book'),
    path('delete_book/<int:id>',delete_book,name='delete_book'),
]
