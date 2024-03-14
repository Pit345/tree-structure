from django.db import models

# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()