from django.db import models

# Create your models here.
# print(models)
class flight (models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
    