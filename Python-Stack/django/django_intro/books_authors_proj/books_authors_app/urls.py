from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.books_index, name="books_index"),
    path("create_book", views.create_book, name="create_book"),
    path("books/<int:book_id>", views.view_book, name="view_book"),
    path(
        "books/<int:book_id>/add_author",
        views.add_author_to_book,
        name="add_author_to_book",
    ),
    path("authors", views.authors_index, name="authors_index"),
    path("create_author", views.create_author, name="create_author"),
    path("authors/<int:author_id>", views.view_author, name="view_author"),
    path(
        "authors/<int:author_id>/add_book",
        views.add_book_to_author,
        name="add_book_to_author",
    ),
    path("authors/<int:author_id>/delete", views.delete_authors, name="delete_authors"),
]
