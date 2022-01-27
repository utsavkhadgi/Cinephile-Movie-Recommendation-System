from django.shortcuts import render
from django.shortcuts import render

from movies.models import Movie

# Create your views here.
def action(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
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