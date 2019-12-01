from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    modified =  models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=60)
    uri = models.CharField(max_length=200)

class Comic(models.Model):
    name = models.CharField(max_length=80)
    uri = models.CharField(max_length=200)
    character_id = models.ForeignKey(Character, on_delete=models.DO_NOTHING)

class Event(models.Model):
    name = models.CharField(max_length=80)
    uri = models.CharField(max_length=200)
    character_id = models.ForeignKey(Character, on_delete=models.DO_NOTHING)

class Serie(models.Model):
    name = models.CharField(max_length=80)
    uri = models.CharField(max_length=200)
    character_id = models.ForeignKey(Character, on_delete=models.DO_NOTHING)

class Storie(models.Model):
    name = models.CharField(max_length=80)
    uri = models.CharField(max_length=200)
    type = models.CharField(max_length=80)
    character_id = models.ForeignKey(Character, on_delete=models.DO_NOTHING)

class Url(models.Model):
    type = models.CharField(max_length=80)
    uri = models.CharField(max_length=200)
    character_id = models.ForeignKey(Character, on_delete=models.DO_NOTHING)
