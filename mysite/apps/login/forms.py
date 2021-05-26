from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True,
                                      'placeholder': 'Usuario: El que usarás para iniciar sesión'})
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

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UsernameForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    class Meta:
        model = User
        fields = ('username',)


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Nombre de Usuario'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))


class AddSerie(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'required': 'True', 'class': 'input', 'placeholder': 'Título'}))

    season = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Temporada'}))

    chapter = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Capítulo'}))

    image = forms.ImageField(required=False)


class AddFilm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'required': 'True', 'class': 'input', 'placeholder': 'Título'}))

    time = forms.CharField(
        widget=forms.TextInput(attrs={'required': 'True', 'class': 'input', 'placeholder': '01:45:50'}))

    image = forms.ImageField(required=False)


class NewNote(forms.Form):
    id_nota = forms.IntegerField()
    type_nota = forms.CharField()
    nota_text = forms.CharField()