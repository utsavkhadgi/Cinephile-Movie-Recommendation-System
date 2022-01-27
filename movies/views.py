from django.http import request
from django.shortcuts import render
import pickle
import pandas as pd
from movies.models import Movie

# Create your views here.
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'movies/index.html',context)


def details(request, id):
    movie = Movie.objects.get(id=id)
    context = {'movie':movie}
    return render(request, 'movies/details.html',context)

#Recommendated Movies    
movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def recommendation(request,title):
  movie = Movie.objects.get(title=title)
  context = {'movie':movie}

  index=movies[movies['title']==movie].index[0]
  similarity_score=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x : x[1])
  recommended_movies = []
  for i in similarity_score[1:6]:
      recommended_movies.append(movies.iloc[i[0]].title)

  return render(request, 'movies/recommandation.html',recommended_movies,context)

 
  




