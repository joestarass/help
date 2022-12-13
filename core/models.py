from django.db import models

class Author(request):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Book(request):
    name = models.CharField(max_length=255)
    count = models.IntegerField()
