from django.shortcuts import render

from movies.models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'searchData/index.html',context)