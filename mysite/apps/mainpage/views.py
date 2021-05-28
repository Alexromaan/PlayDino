from django import forms
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.forms import PasswordChangeForm
from .imdb import search, search_by_id
from .models import Series, Films, Fetch, Image
from apps.login.forms import AddSerie, AddFilm, UserChangeForm

# Create your views here.
from ..login.forms import NewNote, UsernameForm, NewImage


@login_required(login_url=reverse_lazy('login:mainlogin'))
def inicio(request):
    notas_form = NewNote()
    usuario = request.user
    series = Series.objects.filter(user=usuario)
    films = Films.objects.filter(user=usuario)
    context = {'series': series, 'films': films, 'form': notas_form}
    return render(request, 'mainpage/inicio.html', context)


@login_required(login_url=reverse_lazy('login:mainlogin'))
def perfil(request):
    usuario = request.user
    image = Image.objects.filter(user=usuario)
    user_form = UserChangeForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)
    if image.exists():
        ctx = {
        'usuario': usuario,
        'image': Image.objects.get(user=usuario),
        'form': user_form,
        'password_form': password_form
        }
    else:
        ctx = {
            'usuario': usuario,
            'form': user_form,
            'password_form': password_form
        }
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'CAMPO(S) MODIFICADOS CON ÉXITO')
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
            messages.success(request, 'Añadido con éxito')
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
            messages.success(request, 'Añadido con éxito')
            return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/add.html', data)


@login_required(login_url=reverse_lazy('login:mainlogin'))
def delete_serie(request, pk):
    serie = Series.objects.get(id=pk)
    if request.method == 'POST':
        serie.delete()
        messages.success(request, "Eliminado con éxito")
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/delete.html', {'serie': serie})


@login_required(login_url=reverse_lazy('login:mainlogin'))
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
            messages.success(request, "Serie modificada con éxito.")
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/edit_serie.html', data)


@login_required(login_url=reverse_lazy('login:mainlogin'))
def delete_film(request, pk):
    film = Films.objects.get(id=pk)
    if request.method == 'POST':
        film.delete()
        messages.success(request,"Eliminado con éxito")
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/delete.html', {'film': film})


@login_required(login_url=reverse_lazy('login:mainlogin'))
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
            messages.success(request, 'Pelicula modificada con éxito')
        return redirect(to='mainpage:inicio')
    return render(request, 'mainpage/edit_film.html', data)


@login_required(login_url=reverse_lazy('login:mainlogin'))
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
            data = {'message': "No se han encontrado resultados para: ", 'keyword': keyword}
            return render(request, 'mainpage/fetch.html', data)
    # este return es para cuando el request:method = GET, va sin parametros
    return render(request, 'mainpage/fetch.html')


@login_required(login_url=reverse_lazy('login:mainlogin'))
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


@login_required(login_url=reverse_lazy('login:mainlogin'))
def add_note(request):
    if request.method == 'POST':
        nueva_nota = NewNote(request.POST)

        if nueva_nota.is_valid():
            id_nota = nueva_nota.cleaned_data['id_nota']
            nota = nueva_nota.cleaned_data['nota_text']
            type = nueva_nota.cleaned_data['type_nota']

            if type == 'serie':
                serie = Series.objects.get(id=id_nota)
                serie.nota = nota
                serie.save()
                messages.success(request, 'Nota añadida con éxito')

            if type == 'pelicula':
                film = Films.objects.get(id=id_nota)
                film.nota = nota
                film.save()
                messages.success(request, 'Nota añadida con éxito')

    return redirect(to='mainpage:inicio')


@login_required(login_url=reverse_lazy('login:mainlogin'))
def change_username(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            newusername = form.cleaned_data['username']
            user = User.objects.get(username=request.user.username)
            user.username = newusername
            user.save()
            messages.success(request, 'Nombre de usuario actualizado con éxito')
        else:
            messages.error(request,'El nombre de usuario ya está en uso.')
    return redirect(to='mainpage:perfil')


@login_required(login_url=reverse_lazy('login:mainlogin'))
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'La contraseña se ha cambiado con éxito!')
            return redirect(to='mainpage:perfil')
        else:
            messages.error(request, 'Campo(s) introducidos incorrectos.')
    return redirect(to='mainpage:perfil')


@login_required(login_url=reverse_lazy('login:mainlogin'))
def set_image(request):
    if request.method == 'POST':
        form = NewImage(request.POST, request.FILES)
        if form.is_valid():
            newimage = form.cleaned_data['image']

            if Image.objects.filter(user=request.user).exists():
                current_image = Image.objects.get(user=request.user)
                current_image.image = newimage
                current_image.save()
                messages.success(request, 'Foto de Perfil actualizada con éxito!')
            else:
                image = Image(
                    user=request.user,
                    image=newimage
                )
                image.save()
        else:
            messages.error(request,'Imagen no válida.')
    return redirect(to='mainpage:perfil')
