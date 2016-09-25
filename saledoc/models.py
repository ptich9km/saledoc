from django.db import models
from django.utils import timezone


class Post(models.Model):
    name_document = models.TextField()
    soderjanie = models.TextField()

    def preobrazovanie(self):
        self.published_date = timezone.now()
        self.save()

    def podstanovka(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name_document
