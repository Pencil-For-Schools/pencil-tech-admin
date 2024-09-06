from django.db import models

class County(models.Model):
    name = models.CharField(max_length=255)
