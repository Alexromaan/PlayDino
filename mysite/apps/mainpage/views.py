from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from mysite.apps.login.forms import UpdateUser, AñadirSerie

from .models import Series


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


@login_required(login_url=reverse_lazy('login:mainlogin'))
def perfil(request):
    form = UpdateUser()
    meta = list(request.user.filter())
    user_data: {
        'form': form,
        'meta': meta,
    }
    return render(request, 'perfil.html', user_data)


def add_series(request):
    data = {
        'form': AñadirSerie(),
    }
    if request.method == 'POST':
        formulary = AñadirSerie(data=request.POST)
        nueva_serie = Series.create_series(
            name=formulary.cleaned_data['name'],
            platform=formulary.cleaned_data['platform'],
            image=formulary.cleaned_data['image'],
            season=formulary.cleaned_data['season'],
            chapter=formulary.cleaned_data['chapter'],
        )

        if nueva_serie.is_valid():
            nueva_serie.save()
            return redirect(to='mainpage')
        data['form'] = formulary
    return render(request, 'series.html', data)
