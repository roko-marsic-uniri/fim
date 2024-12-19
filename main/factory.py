## factory.py
import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
class FilmFactory(DjangoModelFactory):
    class Meta:
        model = Film

    title = factory.Faker("sentence", nb_words=3) 
    release_date = factory.Faker("date_this_century")  
    genre = factory.Faker("word")  
    director = factory.Faker("name")  
    description = factory.Faker("paragraph") 
    duration = factory.Faker("random_int", min=60, max=180)  
    poster_url = factory.Faker("image_url")  
    created_at = factory.Faker("date_time_this_year")  
    updated_at = factory.Faker("date_time_this_year")