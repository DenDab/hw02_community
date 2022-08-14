from django.shortcuts import render, get_object_or_404
from .models import Post, Group


x=10
def index(request):
    """Открытие главной страницы."""
    template = 'posts/index.html'
    # Коллекция постов, отсортированных по дате, ограниченны 10 шт.
    posts = Post.objects.order_by('-pub_date')[:x]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Открытие страницы c постами, отфильтрованными по группам."""
    template = 'posts/group_list.html'
    # Переменная для отображения ошибки в случае попытки открыть
    # страницу несуществующей группы
    group = get_object_or_404(Group, slug=slug)
    # Коллекция постов отфильтрованных по группе, отсортированных по
    # дате, ограниченны 10 шт.
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:x]
    # Текст для основного блока
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
