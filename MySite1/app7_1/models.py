from django.db import models

# Create your models here.

class Book(models.Model):
    bookid = models.IntegerField(primary_key=True)
    booktitle=models.CharField(max_length=50)
    bookauthor = models.CharField(max_length=50)

    def __str__(self):
        return str(self.bookid)+", "+self.booktitle+", "+self.bookauthor


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    booktitle= models.CharField(max_length=50)

    class Meta:
        ordering=('name','booktitle')

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.booktitle

