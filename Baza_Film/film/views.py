from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from film.models import Movie, Person, Genre
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_films(request):
    movies = Movie.objects.all().order_by('-year')
    return render(request,  "filmy.html", context={"movies": movies,},)

def film(request,pk):
    movie_id = Movie.objects.get(pk=pk)
    genre = Genre.objects.filter(movie=pk)
    starring = Person.objects.filter(PersonMovie=pk)
    genre_list = []
    for gen in genre:
        genre_list.append(gen)
    starring_list = []
    for star in starring:
        starring_list.append(star)
    return render(request,"film.html", context={"genre": genre_list, "starring":starring, 'movie':movie_id,})


def edit_movie(request,pk):
    try:
        movie = Movie.objects.get(pk=pk)

        if request.method == "POST":
            movie.title = request.POST.get("title")
            movie.year = request.POST.get("year")
            movie.rating = request.POST.get("rating")
            movie.director = request.POST.get("director")
            # movie.screenplay = request.POST.get("screenplay")
            movie.save()
            return HttpResponse(f"Dodano film: {movie.title} {movie.year}, {movie.year}, {movie.year}, {Movie.year}, "
                                f"{movie.year}{movie.director}{movie.screenplay}<br>"
                            f'Powrót do bazy filmów: <a href="/movies/">Powrót</a>')
        else:
            return render(request, "edit_movie.html", {"movie": movie})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Movie not found</h2>")


@csrf_exempt
def add_movie(request):
    if request.method == "GET":
        return render(request, "add_film.html")
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        director = request.POST.get("director")
        screenplay = request.POST.get("screenplay")
        staring = request.POST.get("staring")
        # genre = request.POST.get("genre")
        t = Movie()
        t.name = title
        t.year = year
        t.rating = rating
        # t.director = director
        # t.screenplay = screenplay
        # t.starring = staring
        # t.genre = genre.set(genre)
        t.save()
        return HttpResponse(f"Dodano Film: {title} {year} {rating} "
                            f" <br>"
                            f'Powrót do listy filmów: <a href="/movies/">Powrót</a>')


@csrf_exempt
def movies(request):


   if request.method == "GET":
       if request.session.get("sorted") == 1:
           movies = Movie.objects.all().order_by('-rating')
           response = render(request, "movies.html", {"movies": movies})
           return HttpResponse(response)
       if request.session.get("sorted") == 2:
           movies = Movie.objects.all().order_by('rating')
           response = render(request, "movies.html", {"movies": movies})
           return HttpResponse(response)
       if request.session.get("sorted") == 0:
           movies = Movie.objects.all().order_by('year')
           response = render(request, "movies.html", {"movies": movies})
           return HttpResponse(response)
       else:
           movies = Movie.objects.all().order_by('year')
           response = render(request, "movies.html", {"movies": movies})
           return HttpResponse(response)
   if request.method == "POST":
       if request.POST.get("sort") == "highest":
           request.session["sorted"] = 1
           movies = Movie.objects.all().order_by('-rating')
           response = render(request, "movies.html", {"movies": movies})
           return HttpResponse(response)
       if request.POST.get("sort") == "lowest":
           request.session["sorted"] = 2
           movies = Movie.objects.all().order_by('rating')
           response = render(request, "movies.html", {"movies": movies})
           return HttpResponse(response)
       if request.POST.get("sort") == "default":
           request.session["sorted"] = 0
           return HttpResponseRedirect("/movies")


def persons(request):
    lista_osob = ""
    osoby = Person.objects.all().order_by('id')
    for person in osoby:
        lista_osob += f'{person.id}. {person.name} {person.last_name} <a href="/edit_person/{person.id}">edit</a><br>'
    return HttpResponse (f'{lista_osob} <br><a href="/add_person">Dodaj osobę</a><br>'
                         f'<a href="/movies/">Lista filmów</a>')



@csrf_exempt
def add_person(request):
    if request.method == "GET":
        return render(request, "persons.html")
    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        t = Person()
        t.name = name
        t.last_name = last_name
        t.save()
        return HttpResponse(f"Dodano osobę: {name} {last_name}<br>"
                            f'Powrót do listy osób: <a href="/persons/">Powrót</a>')

@csrf_exempt
def edit_person(request,pk):
    try:
        person = Person.objects.get(pk=pk)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.last_name = request.POST.get("last_name")
            person.save()
            return HttpResponse(f"Dodano osobę: {person.name} {person.last_name}<br>"
                            f'Powrót do listy osób: <a href="/persons/">Powrót</a>')
        else:
            return render(request, "edit_person.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def search_movie(request):
    search_query = request.GET.get('search', '')
    founded_movies
    if search_query:
        movie = Movie.object.filter(title__icontaints=search_query)
    else:
        movie = Movie.objects.all()

    return render(request, "movie_search.html", context={"movie": movie,}, )

def count(request):
     person = Person.objects.count()
     return HttpResponse(request, f"Liczba osób: {person} ")