from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Film(models.Model):
    naslov = models.CharField(max_length=100)
    godina = models.IntegerField()
    redatelj = models.CharField(max_length=100)
    zanr = models.CharField(max_length=100)
    preporuceni_filmovi = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='preporuke')

    def __str__(self) -> str:
        return self.naslov

    def prosjecna_ocjena(self):
        return self.recenzija_set.aggregate(models.Avg('ocjena'))['ocjena__avg']

class Recenzija(models.Model):
    ime = models.CharField(max_length=100)
    ocjena = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    text = models.TextField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.ime} - {self.film.naslov}"