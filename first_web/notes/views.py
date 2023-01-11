from django.shortcuts import render
from .models import Articles


def notes_home(request):
    notes = Articles.objects.all()
    return render(request, 'notes/notes_home.html', {'notes': notes})
