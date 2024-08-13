from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    filmler = Film.objects.all()

    context = {
        'filmler':filmler
    }

    return render(request, "index.html", context)

def userRegister(request):
    return render(request, "register.html")