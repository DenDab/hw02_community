"""posts URL Configuration
"""

from django.urls import path

from . import views

# имя namespace из родительского urls.py
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
