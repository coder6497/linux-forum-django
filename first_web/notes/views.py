from django.shortcuts import render


def notes_home(request):
    return render(request, 'notes/notes_home.html')
