from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Класс для хранения таблицы групп блогеров."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # адрес
    description = models.TextField()

    def __str__(self):
        '''Метод для вывода поля title при печати объекта модели Group.'''
        return '%s' % (self.title)


class Post(models.Model):
    """Класс для хранения таблицы сообщений."""

    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # Атрибут-ссылка на модель Групп блогеров
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts'
    )

    def __str__(self):
        """Метод для вывода поля text при печати объекта модели Post."""
        return self.text
