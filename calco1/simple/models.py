from django.db import models

# Create your models here.
class IP(models.Model):
    ip = models.IntegerField()
    browsing = models.CharField(max_length=30)

    def __str__(self):
        return self.ip

class Regeling(models.Model):
    naam = models.CharField(max_length=30)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.naam

class Persoon(models.Model):
    naam = models.CharField(max_length=30)
    leeftijd = models.IntegerField()
    contactmomenten = models.ManyToManyField(Regeling, null=True, related_name="contact_reg")
    lopend = models.ManyToManyField(Regeling, null=True, related_name="lopend_reg")
    browsing = models.ManyToManyField(Regeling, null=True, related_name="browsing_reg")

    def __str__(self):
        return self.naams
