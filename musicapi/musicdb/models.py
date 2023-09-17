from django.conf import settings
from django.db import models
from django.utils import timezone


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.artist_name