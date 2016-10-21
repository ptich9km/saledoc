from django.db import models
from django.utils import timezone


class Post(models.Model):
	name_document = models.TextField()
	soderjanie = models.TextField()
	def __str__(self):
		return self.name_document


