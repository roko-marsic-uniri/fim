from django.db import models
from django.utils import timezone

class Film(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.IntegerField(null=True, blank=True)
    poster_url = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

