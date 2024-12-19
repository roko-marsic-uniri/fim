from django.urls import path
from .views import FilmListView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path("filmovi/", FilmListView.as_view(), name="film_list"),
]