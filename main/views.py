from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from main.models import Film
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

    return render(request, 'registration/register.html', context)

def index(request):
    return render(request, 'main/index.html')

class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"  # Customize the template name as needed
    context_object_name = "films"
    paginate_by = 10  # Number of films per page

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search", "")
        genre_filter = self.request.GET.get("genre", "")

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(director__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        if genre_filter:
            queryset = queryset.filter(genre__icontains=genre_filter)

        return queryset