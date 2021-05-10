from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from .forms import CustomUserCreationForm, LoginForm


def mainlogin(request):
    data = {
        'form': LoginForm(),
    }
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
            user = authenticate(username=formulario.cleaned_data['username'],
                                password=formulario.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('mainpage:inicio'))
    return render(request, 'login/login.html', data)

#parece que funciona
def logout_home(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:mainlogin'))


def RegistroUsuario(request):
    data = {
        'form': CustomUserCreationForm(),
    }
    if request.method == 'POST':

        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],
                                password=formulario.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse('login:mainlogin'))
        data['form'] = formulario
    return render(request, 'login/registro.html', data)

def MostrarUsuario(request):
    return render(request, 'mainpage/perfil.html')
