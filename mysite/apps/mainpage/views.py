from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .imdb import search, search_by_id
from .models import Series, Films, Fetch, Image
from apps.login.forms import AddSerie, AddFilm, UserChangeForm


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
    usuario = request.user
    image = Image.objects.filter(user=usuario)
    ctx = {
        'usuario': usuario,
        'image': image
    }
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(to='mainpage:perfil')
    return render(request, 'mainpage/perfil.html', ctx)


@login_required(login_url=reverse_lazy('login:mainlogin'))
def add(request):
    data = {
        'Serieform': AddSerie(),
        'Filmform': AddFilm()
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


def add_note(request):
    return request


def fetch(request):
    # Aqui trabajaremos con la api de IMDB por lo que hago el parametro global
    global data
    if request.method == 'POST':
        # el modelo Fetch es auxiliar por lo que cada vez que se carga la pagina se elimina
        Fetch.objects.all().delete()

        # recojo el titulo introducido
        keyword = request.POST.get('title')
        # search es el metodo de la api imdb.py
        json = search(keyword)

        # si se devuelven resultados
        if json['Response'] != "False":
            resultset = json['Search']
            # recorro los resultados y los añado a la tabla Fetch
            for result in resultset:
                variable = Fetch(
                    title=result['Title'],
                    image=result['Poster'],
                    imdb=result['imdbID'],
                    type=result['Type']
                )
                variable.save()
                total = Fetch.objects.all()
                data = {
                    'keyword': keyword,
                    'fetch': total
                }
            return render(request, 'mainpage/fetch.html', data)
        else:
            # en el caso de que la api no encuentre nada, mando este mensaje
            data = {'name': "No se han encontrado resultados para: ", 'keyword': keyword}
            return render(request, 'mainpage/fetch.html', data)
    # este return es para cuando el request:method = GET, va sin parametros
    return render(request, 'mainpage/fetch.html')


def save_fetch(request, pk):
    # saco todos los datos de la pelicula/serie elegida y compruebo su tipo de contenido
    json = search_by_id(pk)

    if json['Type'] == "movie":
        nueva_peli = Films(
            name=json['Title'],
            user=request.user,
            image=json['Poster']
        )
        nueva_peli.save()
        messages.success(request, 'HAS AÑADIDO LA PELÍCULA CORRECTAMENTE')
        return redirect(to='mainpage:inicio')

    if json['Type'] == "series":
        nueva_serie = Series(
            name=json['Title'],
            user=request.user,
            image=json['Poster'],
        )
        nueva_serie.save()
        messages.success(request, 'HAS AÑADIDO LA SERIE CORRECTAMENTE')
        return redirect(to='mainpage:inicio')
    messages.error(request, 'NO SE HA PODIDO AÑADIR')
    return redirect(to='mainpage:inicio')
