from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# def post_image(instance,filename):
#     return f'movies/poster/{filename}'


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    releasedDate = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    genre = models.CharField(max_length=100,null=True)
    rating = models.FloatField(
                default=1,
                validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    description = models.TextField()
    org_language = models.CharField(max_length=200,null=True)
    director = models.CharField(max_length=50,null=True)
    cast = models.CharField(max_length=100,null=True)
    tags = models.CharField(max_length=1000,null=True)
    trailer = models.URLField(null=True)

    

    

    def __str__(self):
        return self.title
    # poster = models.ImageField(upload_to=post_image