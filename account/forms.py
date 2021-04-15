from django import forms
from .models import Profile
from localflavor.br.forms import BRStateChoiceField
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        help_texts = {
            'username': None,
        }


class ProfileCreateForm(forms.ModelForm):
    state = BRStateChoiceField(label='Estado')
    date_of_birth = forms.DateField(
        label='Data de nascimento',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Profile
        fields = ('full_name', 'date_of_birth', 'state', 'city')
        labels = {
            'full_name': 'Nome completo',
            'city': 'Cidade',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'date_of_birth', 'state', 'city', 'photo')
        labels = {
            'full_name': 'Nome completo',
            'city': 'Cidade',
            'photo': 'Foto de perfil',
            'state': 'Estado',
            'date_of_birth': 'Data de nascimento',
        }
