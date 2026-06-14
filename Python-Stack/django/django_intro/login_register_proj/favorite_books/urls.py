from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books_index, name='books_index'),
    path('books/create', views.create_book, name='create_book'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/update', views.update_book, name='update_book'),
    path('books/<int:book_id>/delete', views.delete_book, name='delete_book'),
    path('books/<int:book_id>/favorite', views.add_favorite, name='add_favorite'),
    path('books/<int:book_id>/unfavorite', views.remove_favorite, name='remove_favorite'),
    path('user/favorites', views.user_favorites, name='user_favorites'),
]