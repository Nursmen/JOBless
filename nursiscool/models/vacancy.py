from django.db import models
from .ouruser import OurUser
# Create your models here.
from django.conf import settings
from django.utils import timezone

class Vacancy(models.Model):
    title = models.CharField(max_length =250)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    users = models.ManyToManyField(OurUser, related_name="vacancies")