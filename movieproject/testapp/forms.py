from django import forms
from django.forms import ModelForm
from .models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        field='__all__'
