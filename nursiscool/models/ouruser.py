from django.db import models

# Create your models here.
from django.conf import settings

class OurUser(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=25)
    rating = models.FloatField()
    role_choices = {
        "1": "guest",
        "2": "admin",
        "3": "worker",
    }
    role = models.CharField(max_length=1, choices=role_choices, default=role_choices["1"])
    profile_img = models.ImageField(upload_to="img/", blank=True, null=True)

    def __str__(self):
        return self.name