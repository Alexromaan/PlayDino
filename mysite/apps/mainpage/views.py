from django.shortcuts import render

# Create your views here.
def inicio():
    return HttpResponseRedirect(reverse('base.html'))