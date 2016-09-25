from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    file = models.FileField(upload_to=None, max_length=100)

    def preobrazovanie(self):
        self.published_date = timezone.now()
        self.save()

    def podstanovka(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
