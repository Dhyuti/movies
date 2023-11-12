from django.db import models

# Create your models here.

class movies:
    ids: int
    name: str
    img:str
    genre: str
    rating: float


class member(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
