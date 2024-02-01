from django.contrib import admin
from . models import (City, Genre, Author, Book)
# Register your models here.

admin.site.register((City, Genre, Author, Book))
