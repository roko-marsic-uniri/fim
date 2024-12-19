import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Film
from main.factory import (
    FilmFactory,
)

NUM_FILMS = 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Film]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_FILMS):
            author = FilmFactory()