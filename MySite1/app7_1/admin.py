from django.contrib import admin
from .models import Book
from .models import Author
# Register your models here.

# Style-1
admin.site.register(Book)

# Style-2
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'booktitle')