from django.db import models
class Recipe(models.Model):
    Title = models.CharField(max_length=64)
    Ingredients = models.CharField(max_length=255)
    Text = models.CharField(max_length=1000)
    Preparation_Time = models.IntegerField()

# Create your models here.
