from django.contrib import admin
from .models import Book_model, Author, Genre


class Book_modelAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_file_text', 'book_file_audio', 'date_add', 'is_published','cover', 'gener',
                    'Author', 'audio_version', 'text_version', 'date_of_publication')
    list_display_links = ('book_name', 'book_file_text', 'book_file_audio', 'date_add', 'is_published','cover', 'gener',
                    'Author', 'audio_version', 'text_version', 'date_of_publication')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    list_display_links = ('name', 'country',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Book_model)
admin.site.register(Author)
admin.site.register(Genre)
