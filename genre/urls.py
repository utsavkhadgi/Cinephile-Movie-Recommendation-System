from django.urls import path
from . import views

app_name = 'genre'

urlpatterns = [
    path('',views.action,name = 'action'),
    path('comedy',views.comedy,name = 'comedy'),
    path('drama',views.drama,name = 'drama'),
    path('thriller',views.thriller,name = 'thriller'),
    path('adventure',views.adventure,name = 'adventure'),
    path('romance',views.romance,name = 'romance'),
    path('crime',views.crime,name = 'crime'),
    path('sciencefiction',views.sciencefiction,name = 'sciencefiction'),

]