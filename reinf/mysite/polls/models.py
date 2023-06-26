from django.db import models

# Create your models here.
class usuarios(models.Model): 
    user = models.CharField(max_length=15, null=False, blank=False)
    senha = models.CharField(max_length=12, null=False, blank=False)

    