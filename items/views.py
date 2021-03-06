from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import (
    MovieCreateForm,
    BookCreateForm,
    SeriesCreateForm,
    EvaluationForm,
)
from django.contrib import messages
from django.views.generic import DetailView
from .models import Item, Evaluation  # , Like
from django.urls import reverse
from django.db.models import Avg


@login_required()
def register_movie(request):
    if request.method == 'POST':
        form = MovieCreateForm(request.POST)

        if form.is_valid():
            saved = form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )

        return HttpResponseRedirect(reverse(detail, args=(saved.id,)))
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
            saved = form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )
        return HttpResponseRedirect(
            reverse(detail, args=(saved.id,))
        )  # f'items/{saved.id}')
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
            saved = form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )
        return HttpResponseRedirect(reverse(detail, args=(saved.id,)))
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


def detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    latest_eval = Evaluation.objects.filter(item=item_id).order_by('-created')[
        :4
    ]
    average = _parse_average(
        Evaluation.objects.filter(item=item_id)
        .aggregate(Avg('rating'))
        .get('rating__avg')
    )

    print(latest_eval)
    print(len(latest_eval))
    for eval_ in latest_eval:
        print(eval_.id)
    return render(
        request,
        'items/detail.html',
        {
            'object': item,
            'latest_eval': latest_eval,
            'average': average,
            'section': 'detail',
        },
    )


@login_required()
def evaluation(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    average = _parse_average(
        Evaluation.objects.filter(item=item_id)
        .aggregate(Avg('rating'))
        .get('rating__avg')
    )
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.item = item
            temp.save()
            messages.success(request, 'Avaliação realizada com sucesso!')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro na seu avaliação. Verifique os campos e tente novamente!',
            )
        return HttpResponseRedirect(reverse(detail, args=(item_id,)))

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


@login_required()
def like(request):
    print("ENTER")
    print(request.POST.get('eval_id'))
    if request.method == 'POST':

        # item = get_object_or_404(Item,)
        eval_obj = get_object_or_404(
            Evaluation, id=request.POST.get('eval_id')
        )

        liked = None

        if request.user in eval_obj.likes.all():
            eval_obj.likes.remove(request.user)
            liked = False
        else:
            eval_obj.likes.add(request.user)
            liked = True

        item_id = eval_obj.item.id

        res = {'likes': eval_obj.likes.count(), 'liked': liked}
        print("OK")
        return JsonResponse(
            res,
        )


def _parse_average(average):
    average = '%.1f' % average if average else "-,-"
    average = average.replace('.', ',')
    return average
