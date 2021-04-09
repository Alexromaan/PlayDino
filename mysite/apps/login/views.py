from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.urls import reverse
from .forms import CustomUserCreationForm

def login_home(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'login.html')

        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('mainpage:home'))

    if request.method == 'POST':

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('login.html'))


def logout_home(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:mainlogin'))


def RegistroUsuario(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to='login')
        data['form'] = formulario
    return render(request, 'registro.html', data)
