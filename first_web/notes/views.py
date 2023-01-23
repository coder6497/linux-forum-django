from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def notes_home(request):
    notes = Articles.objects.all()
    return render(request, 'notes/notes_home.html', {'notes': notes})


def create_note(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(data=request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            print(form.errors)
            error = "Неверные данные формы"

    form = ArticlesForm
    data = {
        "form": form,
        "error": error
    }
    return render(request, 'notes/create_note.html', data)

