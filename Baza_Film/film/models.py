from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Movie(models.Model):

    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='director')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='screenplay')
    starring = models.ManyToManyField(Person, related_name='PersonMovie')
    year = models.IntegerField(null=True)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title} {self.director} {self.genre}"

