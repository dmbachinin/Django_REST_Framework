from django.db import models
from uuid import uuid4


# Create your models here.
class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.PositiveIntegerField()
