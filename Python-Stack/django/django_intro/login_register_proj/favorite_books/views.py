from django.shortcuts import render, redirect
from django.contrib import messages
from login_register_app.models import User
from .models import Book

def books_index(request):
    if 'user_id' not in request.session:
        return redirect("/")
        
    context = {
        "current_user": User.objects.get(id=request.session['user_id']),
        "all_books": Book.objects.all(),
        "hold_title": request.session.pop('hold_book_title', ''),
        "hold_desc": request.session.pop('hold_book_desc', ''),
    }
    return render(request, 'books_index.html', context)

def create_book(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            request.session['hold_book_title'] = request.POST.get('title', '')
            request.session['hold_book_desc'] = request.POST.get('desc', '')
            return redirect("/books")
            
        user_obj = User.objects.get(id=request.session['user_id'])
        new_book = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            uploaded_by=user_obj
        )
        new_book.users_who_like.add(user_obj)
        messages.success(request, "Book successfully added and favorited!")
        
    return redirect("/books")

def book_detail(request, book_id):
    if 'user_id' not in request.session:
        return redirect("/")
        
    book_obj = Book.objects.get(id=book_id)
    user_obj = User.objects.get(id=request.session['user_id'])
    
    context = {
        "book": book_obj,
        "current_user": user_obj,
        "is_favorited": user_obj in book_obj.users_who_like.all()
    }
    return render(request, 'book_detail.html', context)

def update_book(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        if book.uploaded_by.id == request.session['user_id']:
            errors = Book.objects.book_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
            else:
                book.title = request.POST['title']
                book.desc = request.POST['desc']
                book.save()
                messages.success(request, "Book updated successfully.")
        return redirect(f"/books/{book_id}")

def delete_book(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        if book.uploaded_by.id == request.session['user_id']:
            book.delete()
            messages.success(request, "Book deleted successfully.")
    return redirect("/books")

def add_favorite(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=request.session['user_id'])
        book.users_who_like.add(user)
    return redirect(request.META.get('HTTP_REFERER', '/books'))

def remove_favorite(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=request.session['user_id'])
        book.users_who_like.remove(user)
    return redirect(request.META.get('HTTP_REFERER', '/books'))

def user_favorites(request):
    if 'user_id' not in request.session:
        return redirect("/")
        
    user_obj = User.objects.get(id=request.session['user_id'])
    context = {
        "current_user": user_obj,
        "my_favorite_books": user_obj.liked_books.all()
    }
    return render(request, 'user_favorites.html', context)