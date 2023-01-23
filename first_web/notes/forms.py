from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'date_time', 'user_name']
        widgets = {"title": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Название темы"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст темы"
            }),
            "date_time": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Дата создания"
            }),
            "user_name": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Пользователь"
            })}
