from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=200)


class Genre(models.Model):
    name = models.CharField(max_length=200)


class Book_model(models.Model):
    book_name = models.CharField(max_length=250)
    book_file_text = models.FileField(upload_to='book')
    book_file_audio = models.FileField(upload_to='book_audio')
    date_add = models.DateTimeField(auto_now_add=True)
    is_published =models.BooleanField()
    cover = models.FileField(upload_to='book_image')
    genre =models.ForeignKey(Genre, on_delete=models.CASCADE)
    Author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    audio_version = models.BooleanField()
    text_version = models.BooleanField()
    date_of_publication = models.DateField()
