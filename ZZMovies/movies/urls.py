from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path('movies/', views.get_movies),
    path('upload_movies',views.movie_upload),
    path('movie_detail/<int:movie_id>',views.get_movie_detail)


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)