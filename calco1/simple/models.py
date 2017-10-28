from django.db import models

# Create your models here.
class Regelingen(models.Model):
    naam = models.CharField(max_length=30)
    update_url = models.CharField(max_length=100)
    insert_url = models.CharField(max_length=100)
    info_url = models.CharField(max_length=100)

    def __str__(self):
        return self.naam

class Persoon(models.Model):
    naam = models.CharField(max_length=30)
    geslacht = models.CharField(max_length=1)
    leeftijd = models.IntegerField()
    werkend = models.BooleanField()
    ontslagaanvraag = models.BooleanField()
    regelingen = models.ManyToManyField(Regelingen, related_name="lopend_reg")
    
    def __str__(self):
        return self.naam

