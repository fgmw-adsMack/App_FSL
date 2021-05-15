from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import UserCreateForm, ProfileCreateForm, ProfileEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.generic import DetailView
from .models import Profile


def index(request):
    return render(request, 'account/index.html')


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@transaction.atomic
def creation_user_profile(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        profile_form = ProfileCreateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # Carrega o perfil criado pela signal
            profile_form = ProfileCreateForm(
                request.POST, instance=user.profile
            )  # Volta a carregar formulário do Profile pela instância Profile
            profile_form.full_clean()  # Limpa o formulário. Chama is_valid()
            profile_form.save()  # Salva o formulário

            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, 'Bem-vindo para a FSL!')
            return redirect('dashboard')
        else:
            messages.error(
                request,
                'Ops! Aconteceu um erro no seu cadastro. Verifique os campos e tente novamente!',
            )

    else:
        user_form = UserCreateForm()
        profile_form = ProfileCreateForm()
    return render(
        request,
        'account/signup.html',
        {'user_form': user_form, 'profile_form': profile_form},
    )


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Seus dados formam atualizados com sucesso!'
            )
        else:
            messages.error(request, 'Por favor, verifique os campos.')
    else:
        form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        'account/update_profile.html',
        {'profile_edit_form': form, 'section': 'configuration'},
    )


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(
                request, user
            )  # mantem a sessão do usuário
            messages.success(
                request, 'Sua password foi atualizada com sucesso!'
            )
            return redirect('change_password')
        else:
            messages.error(request, 'Por favor, verifique os campos.')
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request, 'account/change_password.html', {'password_edit_form': form}
    )


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'account/profile_detail.html'
