import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Napitak, Sladoled, Sladoledni_kup
from main.factory import (
    SladoledFactory,
    Sladoledni_kupFactory,
    NapitakFactory
)

NUM_SLAD = 150
NUM_KUP = 50
NUM_NAP = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Sladoled, Sladoledni_kup, Napitak]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_SLAD):
            author = SladoledFactory()

        for _ in range(NUM_KUP):
            book = Sladoledni_kupFactory()

        for _ in range(NUM_NAP):
            book = NapitakFactory()
