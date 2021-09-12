from django import forms
from django.forms import ModelForm
from . models import  MovieUpload, Profile



class MovieForm (forms.Form):
    moviename= forms.CharField(max_length=50)
    description= forms.CharField(max_length=500)
    image= forms.ImageField()
    category= forms.CharField(max_length=10)
    productionyear = forms.DateField()
    movietrailer = forms.URLField()



class UserForm (ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'




class MovieForm(ModelForm):
    class Meta:
        model = MovieUpload
        fields = "__all__"
 