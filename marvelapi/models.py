from django.db import models

class Characters(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    modified =  models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=60)
    uri = models.CharField(max_length=60)
