from traceback import print_tb
from django.http import request
from django.shortcuts import render
import pickle
import pandas as pd
import requests

from movies.models import Movie

# Create your views here.
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    
    poster = []
    for i in movies:
        poster.append(fetch_poster(i.id))

    result = list(zip(movies,poster))
    context = {'result':result}
    # context = {
    #     'movies':movies,
    #     # 'poster':poster,
    #     'result':result,
    #     # 'results':results
    #     }
    return render(request,'movies/index.html',context)


def details(request, id):
    movie = Movie.objects.get(id=id)
    context = {'movie':movie}
    return render(request, 'movies/details.html',context)

#Recommendated Movies    
movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommendation(request, title):
    movie = Movie.objects.get(title=title)
    context = {'movie':movie} 

    index=movies[movies['title']== title].index[0]
    similarity_score=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x : x[1])
    
    res = []
    # ress = []
    recommended_movie_posters = []
    for i in similarity_score[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        res.append(movies.iloc[i[0]].title)
        # ress.append(movies.iloc[i[0]].movie_id)

    
    result = zip(res,recommended_movie_posters)

    # print([i.titleitle for i in res])

    data = {
        # 'res':res,
        'result':result,
        # 'recommended_movie_posters':recommended_movie_posters,
        'movie':movie,
    }  
   
    return render(request, 'movies/recommendation.html',data)








  
  



 
  




