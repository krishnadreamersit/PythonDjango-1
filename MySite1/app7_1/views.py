from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def index(request):
    # use
    # Style-1
    """
    book = Book()
    book.bookid=2
    book.booktitle='Core Python-2'
    book.bookauthor='John'
    book.save()
    """

    # Style-2
    """
    book = Book(3, 'C Programming','Bala Guru S')
    result = book.save()
    print(result)
    """

    # Retrieve all
    books = Book.objects.all()
    """
    for book in books:
        print(book)
    """
    # publish all books in html page
    context = {'books': books}
    return render(request, 'app7_1/index.html', context)