from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Series
from apps.login.forms import AddSerie, UpdateUser


# Create your views here.
@login_required(login_url=reverse_lazy('login:mainlogin'))
def inicio(request):
    return render(request, 'mainpage/mainpage_base.html')


@login_required(login_url=reverse_lazy('login:mainlogin'))
def perfil(request):
    data = {
        'form': UpdateUser(),
    }
    if request.method == 'POST':
        formulation = UpdateUser(data=request.POST)
        if formulation.is_valid():
            formulation.save(),
            return redirect(to='mainpage:perfil')
        data['form'] = formulation
    return render(request, 'mainpage/perfil.html', data)


@login_required(login_url=reverse_lazy('login:mainlogin'))
def add_series(request):
    data = {
        'form': AddSerie(),
    }
    if request.method == 'POST':
        formulary = AddSerie(data=request.POST)
        if formulary.is_valid():
            nueva_serie = Series(
                name=formulary.cleaned_data['name'],
                platform=formulary.cleaned_data['platform'],
                season=formulary.cleaned_data['season'],
                chapter=formulary.cleaned_data['chapter'],
            )
            nueva_serie.save()
            return redirect(to='mainpage:inicio')
        data['form'] = formulary
    return render(request, 'mainpage/series.html', data)
