from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from . utils import make_id
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100, null=False)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    auth_id = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(
        max_length=150, null=True, blank=True, unique=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images/profile/')
    city_model = models.ForeignKey(
        City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.id:
            city, created = City.objects.get_or_create(name=self.city.upper())
            id = make_id(city.name, city.count + 1, 5)
            city.count = F('count') + 1
            city.save()
            self.auth_id = id
            self.city_model = city
            user = User.objects.create_user(
                username=self.username, password=self.password)
            user.save()
            self.user = user
            self.password = ''

        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + " " + self.auth_id

    @property
    def books(self):
        books = self.authors.all()
        return books


class Book(models.Model):
    name = models.CharField(max_length=150)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pages = models.IntegerField()
    cover_image = models.ImageField(
        upload_to='images/cover/', blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='authors')

    def __str__(self):
        return self.name
