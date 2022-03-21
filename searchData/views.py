import imp
from django.shortcuts import render

from movies.models import Movie
import requests
import pickle
import pandas as pd


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))
    result = list(zip(movies,poster))
    if request.method == "POST":
      searched = request.POST['searched']  
      searchedmovie = Movie.objects.get(title=searched)
      postersearch = fetch_poster(searchedmovie.id)
      trailersearch = fetch_trailer(searchedmovie.id)
      data = recommendation(searchedmovie.title)
      context = {
        'movies':movies,
        'result':result,
        'searched':searched,
        'searchedmovie':searchedmovie,
        'postersearch':postersearch,
        'trailersearch':trailersearch,
        'data':data
        }
      return render(request,'searchData/index.html',context)
    else:
      movie = Movie.objects.get(id=id)
      context = {'movie':movie}
      return render(request,'movies/index.html',context)       



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_trailer(movie_id):
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

#Recommendated Movies    
movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def recommendation(title):
    movie = Movie.objects.get(title=title)
    # context = {'movie':movie} 
    index=movies[movies['title']== title].index[0]
    similarity_score=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x : x[1])
    
    res = []
    # resid = []
    recommended_movie_posters = []
    for i in similarity_score[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        res.append(movies.iloc[i[0]].title)
        # resid.append(movies.iloc[i[0]].movie_id,resid)
        # ress.append(movies.iloc[i[0]].movie_id)
  
    result = zip(res,recommended_movie_posters)
    # data = {
    #     # 'res':res,
    #     'result':result,
    #     # 'recommended_movie_posters':recommended_movie_posters,
    #     'movie':movie,
    # }  
    return result

    