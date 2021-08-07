from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Project

def start(request):
    return render(request, 'StartPage.html')


def contact(request):

    return render(request, 'MainAlmatyFilial.html')


def Taldyk(request):
    return render(request, 'filials/Taldykorgan.html')


def Pavlodar(request):
    return render(request, 'filials/Павлодар.html')


def Atyrau(request):
    return render(request, 'filials/Atyrau.html')


def service(request):
    return render(request, 'Service.html')


def projects(request):
    Allprojects = Project.objects.all()
    return render(request, 'Project.html', {'Allprojects': Allprojects})


def aboutUs(request):
    return render(request, 'About us.html')


def review(request):
    return render(request, 'reviews.html')

