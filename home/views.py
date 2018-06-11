from django.shortcuts import render
from .models import Book
from .models import Author

# Create your views here.
def get_index(request):
    
    books = Book.objects.all()
    authors = Author.objects.all()
    
    return render(request, "home/index.html", {'books': books, 'authors': authors})
