from django.urls import path 
from book_app.views import home,store_book,show_books,edit_book,delete_book

urlpatterns = [
    path('',home,name="home"),
    path('store_book/',store_book, name="stores"),
    path('show_book/',show_books, name="show_book"),
    path('edit_book/<int:id>',edit_book, name="edit_book"),
    path('delete_book/<int:id>',delete_book, name="delete_book"),
]
