from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Series, Films
from apps.login.forms import AddSerie, AddFilm


# Create your views here.
@login_required(login_url=reverse_lazy('login:mainlogin'))
def inicio(request):
    usuario = request.user
    series = Series.objects.filter(user=usuario)
    films = Films.objects.filter(user=usuario)
    context = {'series': series, 'films': films}
    return render(request, 'mainpage/inicio.html', context)


@login_required(login_url=reverse_lazy('login:mainlogin'))
def perfil(request):
    return render(request, 'mainpage/perfil.html')


@login_required(login_url=reverse_lazy('login:mainlogin'))
def add(request):
    data = {
        'Serieform': AddSerie(),
        'Filmform':  AddFilm()
    }
    if request.method == 'POST':
        formulary1 = AddFilm(request.POST, request.FILES)
        if formulary1.is_valid():
            nueva_peli = Films(
                name=formulary1.cleaned_data['name'],
                time=formulary1.cleaned_data['time'],
                user=request.user,
                image=formulary1.cleaned_data['image'],
            )
            nueva_peli.save()
            return redirect(to='mainpage:inicio')

        formulary2 = AddSerie(request.POST, request.FILES)
        if formulary2.is_valid():
            nueva_serie = Series(
                name=formulary2.cleaned_data['name'],
                season=formulary2.cleaned_data['season'],
                chapter=formulary2.cleaned_data['chapter'],
                user=request.user,
                image=formulary2.cleaned_data['image'],
            )
            nueva_serie.save()
            return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/add.html', data)


def delete_serie(request, pk):
    serie = Series.objects.get(id=pk)
    if request.method == 'POST':
        serie.delete()
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/delete.html', {'serie': serie})


def edit_serie(request, pk):
    serie = Series.objects.get(id=pk)
    data = {
        'Serieform': AddSerie(),
        'name': serie.name,
        'chapter': serie.chapter,
        'season': serie.season,
    }
    if request.method == 'POST':
        formulary = AddSerie(request.POST)
        if formulary.is_valid():
            nueva_serie = Series(
                name=formulary.cleaned_data['name'],
                season=formulary.cleaned_data['season'],
                chapter=formulary.cleaned_data['chapter'],
                user=request.user,
                id=serie.id,
                image=serie.image
            )
            nueva_serie.save()
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/edit_serie.html', data)


def delete_film(request, pk):
    film = Films.objects.get(id=pk)
    if request.method == 'POST':
        film.delete()
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/delete.html', {'film': film})


def edit_film(request, pk):
    film = Films.objects.get(id=pk)
    data = {
        'Filmform': AddFilm(),
        'name': film.name,
        'time': film.time,
        'film': film.image
    }
    if request.method == 'POST':
        formulary = AddFilm(request.POST)
        if formulary.is_valid():
            nueva_peli = Films(
                name=formulary.cleaned_data['name'],
                time=formulary.cleaned_data['time'],
                user=request.user,
                id=film.id,
                image=film.image,
            )
            nueva_peli.save()
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/edit_film.html', data)
