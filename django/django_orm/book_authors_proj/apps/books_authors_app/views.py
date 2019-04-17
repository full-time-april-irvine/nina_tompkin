"""testing docstring."""

from django.shortcuts import render, redirect
from .models import Books, Authors

def index(request):
    context = {
        "all_books":Books.objects.all()
        }
    return render(request, "books_authors_app/index.html", context)

def add_book(request):
    if request.method == "POST":
        title = request.POST["book_title"]
        desc = request.POST["book_description"]
        new_book = Books.objects.create(title=title, desc=desc)
        book_num = new_book.id
    return redirect(f"/books/{book_num}")

def authors(request):
    context = {
        "all_authors":Authors.objects.all()
        }
    return render(request, "books_authors_app/authors.html", context)

def add_new_author(request):
    if request.method == "POST":
        first = request.POST["fname"]
        last = request.POST["lname"]
        notes = request.POST["notes"]
        new_author = Authors.objects.create(first_name=first,last_name=last,notes=notes)
        author_id = new_author.id
    return redirect(f"/author/{author_id}")

def add_book_to_author(request):
    if request.method == "POST":
        author_id = request.POST["this_author"]
        book_id = request.POST["books"]
        this_book = Books.objects.get(id=book_id)
        this_author = Authors.objects.get(id=author_id)
        this_author.books.add(this_book)
    return redirect(f"/author/{author_id}")

def add_author_to_book(request):
    if request.method =="POST":
        print(request.POST)
        book_id = request.POST["this_book"]
        author_id = request.POST["authors"]
        this_book = Books.objects.get(id=book_id)
        this_author = Authors.objects.get(id=author_id)
        this_author.books.add(this_book)
    return redirect(f"/books/{book_id}")

def author(request, author_id):
    this_author = Authors.objects.get(id=author_id)

    context = {
        "all_books":Books.objects.all(),
        "all_authors":Authors.objects.all(),
        "this_author":Authors.objects.get(id=author_id),
        "these_books":this_author.books.all()
        }

    return render(request, "books_authors_app/display_author.html", context)

def books(request, book_id):
    this_book = Books.objects.get(id=book_id)

    context = {
        "all_books":Books.objects.all(),
        "all_authors":Authors.objects.all(),
        "this_book":Books.objects.get(id=book_id),
        "these_authors":this_book.authors.all()
        }
    return render(request, "books_authors_app/display_book.html", context)