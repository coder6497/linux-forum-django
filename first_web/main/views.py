from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>ДРИСТ</h1>')


def about(request):
    return HttpResponse("<h1>О сайте</h1>")