from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from .forms import CustomUserCreationForm, LoginForm


def mainlogin(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'login/login.html')

        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('mainpage:inicio'))

    data = {
        'form': LoginForm(),
    }
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        data['form'] = formulario
    return render(request, 'login.html', data)


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
            return redirect(to='login')
        data['form'] = formulario
    return render(request, 'registro.html', data)
