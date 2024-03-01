from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class OurUser(models.Model):
    name = models.CharField(max_length=250)
    password = models.IntegerField(max_length =10)
    rating = models.FloatField()

def str(self):
    return self.name