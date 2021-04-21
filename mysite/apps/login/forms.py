from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Nombre de Usuario'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Apellidos'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'email'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirmar Contraseña'}))


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Nombre de Usuario'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))


class UpdateUser(forms.Form):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Nombre de Usuario'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Apellidos'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))

#este formulario falla
class AddSerie(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'required': 'True', 'class': 'input', 'placeholder': 'Título'}))

    platform = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Plataforma'}))

    image = forms.ImageField(
        widget=forms.ImageField())

    season = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Temporada'}))

    chapter = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Capítulo'}))
