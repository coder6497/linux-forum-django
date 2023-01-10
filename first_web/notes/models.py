from django.db import models


class Articles(models.Model):
    title = models.CharField("Название", max_length=80)
    full_text = models.TextField("Тема")
    date_time = models.DateTimeField("Дата публикации")
    user_name = models.CharField("Пользователь", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = 'Темы'