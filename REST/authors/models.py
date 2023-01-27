from django.db import models
from uuid import uuid4


# Create your models here.
class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.PositiveIntegerField()

class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.ManyToManyField(Author)

class Article(models.Model):
    text = models.TextField()
    author = models.ManyToManyField(Author)
