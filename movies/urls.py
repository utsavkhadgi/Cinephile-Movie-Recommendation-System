from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.index, name='index'),
    path('details/<int:id>',views.details,name='details'),
    path('recommendation/<slug:title>',views.recommendation,name='recommendation'),
    # path('top-movies/',views.top_movies,NameError='top-movies'),
    # path('top-series/',views.top_series,NameError='top-series'),
    
]