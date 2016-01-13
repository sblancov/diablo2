from django.db import models


class Helm(models.Model):

    name = models.CharField(max_length=255)
    min_defense = models.IntegerField()
    max_defense = models.IntegerField()
    strenght = models.IntegerField()
    durability = models.IntegerField()
    sockets = models.IntegerField()
    tc = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
