import imp
from django.shortcuts import render

from movies.models import Movie
import requests


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))
    result = list(zip(movies,poster))
    if request.method == "POST":
      searched = request.POST['searched']  
      movietitle = Movie.objects.get(title=searched)
      postersearch = fetch_poster(movietitle.id)
      trailersearch = fetch_trailer(movietitle.id)
      context = {
        'movies':movies,
        'result':result,
        'searched':searched,
        'movietitle':movietitle,
        'postersearch':postersearch,
        'trailersearch':trailersearch
        }
      return render(request,'searchData/index.html',context)
    else:
      movie = Movie.objects.get(id=id)
      context = {'movie':movie}
      return render(request,'movies/index.html',context)       

        
def details(request, id):
    movie = Movie.objects.get(id=id)
    context = {'movie':movie}
    return render(request, 'movies/details.html',context)



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_trailer(movie_id):
    print(movie_id)
    url = "http://api.themoviedb.org/3/movie/{}/videos?api_key=5578e593eff67be13a5e7e2ae5074824".format(movie_id)
    data = requests.get(url)
    data = data.json()
    # trailer_path = data['key']
    # full_path = "https://www.youtube.com/watch?v=" + trailer_path
    # type = "Trailer"
    for da in data['results']:
        if da["type"] == "Trailer":
            trailer_path = da['key']
            full_path = "https://www.youtube.com/embed/" + trailer_path
    return full_path