from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MovieCreateForm, BookCreateForm, SeriesCreateForm
from django.contrib import messages


@login_required()
def register_movie(request):
    if request.method == 'POST':
        form = MovieCreateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(request,
                             'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!')
    else:
        form = MovieCreateForm()
    return render(
        request,
        'items/registration.html',
        {'register_form': form, 'section': 'register', 'item_name': ' - Filme'},
    )

@login_required()
def register_book(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(request,
                             'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!')
    else:
        form = BookCreateForm()
    return render(
        request,
        'items/registration.html',
        {'register_form': form, 'section': 'register', 'item_name': ' - Livro'},
    )

@login_required()
def register_series(request):
    if request.method == 'POST':
        form = SeriesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(request,
                             'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!')
    else:
        form = SeriesCreateForm()
    return render(
        request,
        'items/registration.html',
        {'register_form': form, 'section': 'register', 'item_name': ' - Série'},
    )

@login_required()
def item_detail(request):
    pass
