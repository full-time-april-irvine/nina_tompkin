from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos,related_name="ninjas") 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
