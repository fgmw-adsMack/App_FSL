from django import forms
from .models import Item


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'director', 'cast', 'year', 'country')
        labels = {
            'title': 'Título',
            'director': 'Diretor',
            'cast': 'Elenco principal',
            'year': 'Ano',
            'country': 'País',
        }


class SeriesCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'director', 'cast', 'year', 'country', 'seasons')
        labels = {
            'title': 'Título',
            'director': 'Diretor',
            'cast': 'Elenco principal',
            'year': 'Ano',
            'country': 'País',
            'seasons': 'Temporadas',
        }


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'author', 'publisher', 'year', 'country')
        labels = {
            'title': 'Título',
            'author': 'Autor(es)',
            'publisher': 'Editora',
            'year': 'Ano de lançamento',
            'country': 'País',
        }
