from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MovieCreateForm
from django.contrib import messages


@login_required()
def register(request):
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
        {'register_form': form, 'section': 'register'},
    )


