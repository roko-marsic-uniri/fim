from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from main.models import Film, Review
from .forms import ReviewForm
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'register.html', context)

def home(request):
    search_query = request.GET.get("search", "")
    genre_filter = request.GET.get("genre", "")
    films = Film.objects.all()

    if search_query:
        films = films.filter(
            Q(title__icontains=search_query) |
            Q(director__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if genre_filter:
        films = films.filter(genre__icontains=genre_filter)

    return render(request, 'film_list.html', {'films': films})

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    reviews = film.reviews.all()
    review_form = ReviewForm()

    context = {
        'film': film,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'film_detail.html', context)

@login_required
def add_review(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.film = film
            review.user = request.user
            review.save()
            return redirect('film_detail', pk=film.pk)
    return redirect('film_detail', pk=film.pk)

@login_required
def update_review(request, pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk, film_id=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('film_detail', pk=pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'update_review.html', {'form': form, 'film': review.film})

@login_required
def delete_review(request, pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk, film_id=pk, user=request.user)
    review.delete()
    return redirect('film_detail', pk=pk)