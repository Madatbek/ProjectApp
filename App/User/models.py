from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


