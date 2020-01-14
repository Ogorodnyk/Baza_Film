from django.contrib import admin

# Register your models here.
from film.models import Person, Genre,Movie
admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Movie)