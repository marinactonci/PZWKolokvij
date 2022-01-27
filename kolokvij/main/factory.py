## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE

# moji ce sladoledi, napitci itd imat imena moji prijatelja

class SladoledFactory(DjangoModelFactory):
    class Meta:
        model = Sladoled

    naziv = factory.Faker("first_name")
    datum_proizvodnje = factory.Faker("date_time")
    vegan = factory.Faker("boolean")

class Sladoledni_kupFactory(DjangoModelFactory):
    class Meta:
        model = Sladoledni_kup

    naziv = factory.Faker("first_name")
    cijena = factory.Faker("numerify")
    sladoled = factory.Iterator(Sladoled.objects.all())
    opis = factory.Faker("sentence", nb_words=50)

class NapitakFactory(DjangoModelFactory):
    class Meta:
        model = Napitak

    naziv = factory.Faker("first_name")
    cijena = factory.Faker("numerify")
    drzava = factory.Faker("country")
    opis = factory.Faker("sentence", nb_words=50)
