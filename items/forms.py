from django import forms
from .models import Item, Evaluation


class MovieCreateForm(forms.ModelForm):
    item_type = forms.CharField(widget=forms.HiddenInput(),initial='movie')
    class Meta:
        model = Item
        fields = ('title', 'director', 'cast', 'year', 'country', 'item_type')
        labels = {
            'title': 'Título',
            'director': 'Diretor',
            'cast': 'Elenco principal',
            'year': 'Ano',
            'country': 'País',
        }


class SeriesCreateForm(forms.ModelForm):
    item_type = forms.CharField(widget=forms.HiddenInput(),initial='series')
    class Meta:
        model = Item
        fields = ('title', 'director', 'cast', 'year', 'country', 'seasons', 'item_type')
        labels = {
            'title': 'Título',
            'director': 'Diretor',
            'cast': 'Elenco principal',
            'year': 'Ano',
            'country': 'País',
            'seasons': 'Temporadas',
        }


class BookCreateForm(forms.ModelForm):
    item_type = forms.CharField(widget=forms.HiddenInput(),initial='book')
    #item_type = forms.CharField(initial='book')
    class Meta:
        model = Item
        fields = ('title', 'author', 'publisher', 'year', 'country', 'item_type')
        labels = {
            'title': 'Título',
            'author': 'Autor(es)',
            'publisher': 'Editora',
            'year': 'Ano de lançamento',
            'country': 'País',
        }


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ('rating', 'comment')
        labels = {
            'rating': 'Nota',
            'comment': 'Comentário',
        }
        widgets = {
            #'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Escreva um comentário',
                    'rows': '5',
                    'cols':'150',
                    'class': 'border-control form-control'
                }),
        }