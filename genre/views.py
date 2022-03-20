from django.shortcuts import render
from django.shortcuts import render

from movies.models import Movie
import requests
# Create your views here.
def action(request):
    movies = Movie.objects.all()

    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    return render(request,'genre/action.html',context)

def comedy(request):
    return render(request,'genre/comedy.html')

def drama(request):
    return render(request,'genre/drama.html')

def thriller(request):
    return render(request,'genre/thriller.html')


def adventure(request):
    return render(request,'genre/adventure.html')


def romance(request):
    return render(request,'genre/romance.html')


def crime(request):
    return render(request,'genre/crime.html')


def sciencefiction(request):
    return render(request,'genre/sciencefiction.html')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path