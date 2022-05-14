from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author,verbose_name="authors",related_name='books')
    date = models.IntegerField(max_length=4)
    genres = models.ManyToManyField(Genre,verbose_name="genres",related_name='books')

    def __str__(self):
        return self.name



