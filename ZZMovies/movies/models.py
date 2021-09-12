from django.db import models
from django.core import validators
from django.core.validators import *


# Create your models here.



class Profile (models.Model):
    # if we write null = true, then we haveto migrate otherwise not

    phone= models.CharField(max_length=10, validators=[validators.MinLengthValidator(7)])
    firstsignedin= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.phone


class MovieUpload(models.Model):
    movie_name= models.CharField(max_length=50)
    description= models.CharField(max_length=500)
    file= models.FileField(upload_to='static/uploads')
    image = models.ImageField(upload_to = 'static/banner')
    category= models.CharField(max_length=10)
    productionyear = models.CharField(max_length=30)
    movietrailer = models.URLField(blank=True)

    def __str__(self):
        return  self.movie_name
    