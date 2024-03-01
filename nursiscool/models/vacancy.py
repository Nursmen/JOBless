from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Vacancy(models.Model):
    title = models.CharField(max_length =250)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)