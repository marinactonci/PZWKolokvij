from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE

class Sladoled(models.Model):
    naziv = models.CharField(max_length=30)
    datum_proizvodnje = models.DateField()
    vegan = models.BooleanField()

    def __str__(self):
        return self.naziv

class Sladoledni_kup(models.Model):
    naziv = models.CharField(max_length=30)
    cijena = models.IntegerField(
        default=30,
        validators=[MaxValueValidator(120), MinValueValidator(30)]
    )
    sladoled = models.ForeignKey(Sladoled, on_delete=CASCADE)
    opis = models.TextField()

    def __str__(self):
        return self.naziv

class Napitak(models.Model):
    naziv = models.CharField(max_length=30)
    cijena = models.IntegerField(
        default=10,
        validators=[MaxValueValidator(100), MinValueValidator(10)]
    )
    drzava = models.CharField(max_length=100)
    opis = models.TextField()

    def __str__(self):
        return self.naziv