from django.db import models
from django.urls import reverse


# Create your models here.
class Style(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    era = models.IntegerField()

    def __str__(self):
        return self.title


