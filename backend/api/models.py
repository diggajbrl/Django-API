from django.db import models

# Create your models here.

class Student (models.Model) :
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=150)

    # step 1

    # Source : https://www.youtube.com/watch?v=JQ4fSYu8hCw