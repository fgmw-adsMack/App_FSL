from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MovieCreateForm, BookCreateForm, SeriesCreateForm, EvaluationForm
from django.contrib import messages
from django.views.generic import DetailView
from .models import Item, Evaluation
from django.db.models import Avg


@login_required()
def register_movie(request):
    if request.method == 'POST':
        form = MovieCreateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )
    else:
        form = MovieCreateForm()
    return render(
        request,
        'items/registration.html',
        {
            'register_form': form,
            'section': 'register',
            'item_name': ' - Filme',
        },
    )


@login_required()
def register_book(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )
    else:
        form = BookCreateForm()
    return render(
        request,
        'items/registration.html',
        {
            'register_form': form,
            'section': 'register',
            'item_name': ' - Livro',
        },
    )


@login_required()
def register_series(request):
    if request.method == 'POST':
        form = SeriesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )
    else:
        form = SeriesCreateForm()
    return render(
        request,
        'items/registration.html',
        {
            'register_form': form,
            'section': 'register',
            'item_name': ' - Série',
        },
    )


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/detail.html'

def detail(request,item_id):
    item = Item.objects.get(id=item_id)
    latest = Evaluation.objects.filter(item=item_id).order_by('-created')[:4]
    average = '%.1f' % Evaluation.objects.filter(item=item_id).aggregate(Avg('rating')).get('rating__avg')
    average = average.replace('.',',')
    print(latest)
    print(len(latest))
    # form = Evaluation()
    return render(
        request,
        'items/detail.html',
        {
            'object': item,
            'latest': latest,
            'average': average,
            'section': 'detail',
        },
    )


@login_required()
def evaluation(request,item_id):
    # print("Username: "+str(request))
    item = Item.objects.get(id=item_id)
    average = '%.1f' % Evaluation.objects.filter(item=item_id).aggregate(Avg('rating')).get('rating__avg')
    average = average.replace('.',',')
    if request.method == 'POST':
        # print(request.user.username)
        form = EvaluationForm(request.POST)
        # form.instance.user = request.user
        # form.instance.item = item
        # print(form)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.item = item
            temp.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )
    else:
        form = EvaluationForm()
    return render(
        request,
        'items/evaluation.html',
        {
            'object': item,
            'average': average,
            'evaluation_form': form,
            'section': 'evaluation',
        },
    )