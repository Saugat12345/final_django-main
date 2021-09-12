
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import  MovieUpload
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


# Create your views here.



def get_movies(request):
    movies = MovieUpload.objects.all().order_by("-id")
    context = {
      'movies': movies,
      'activate_movie': 'active'
    }
    return render(request, 'movies/get_movies.html', context)
       


def movie_upload(request):
    if request.method == "POST":
        moviename = request.POST['moviename']
        description = request.POST['description']
        file = request.FILES['file']
        image = request.FILES['image']

        category = request.POST['category']
        productionyear = request.POST['productionyear']
        movietrailer = request.POST['movietrailer']
        movie = MovieUpload.objects.create(
                              movie_name=moviename,description=description,file=file,image=image,category=category,
                              productionyear=productionyear,movietrailer=movietrailer)

        if movie:
           return HttpResponse("done")
        # url path
        else:
            return HttpResponse("Unable to create student")
    context = {
        'activate_student': 'active'
    }
    return render(request, 'movies/get_movie_form.html', context)

   




def get_movie_detail(request,movie_id):
    movie = MovieUpload.objects.get(id = movie_id)
    context = {
      'm': movie,
      'activate_movie': 'active'
    }
   
    return render(request, 'movies/movies_detail.html', context)
    
    