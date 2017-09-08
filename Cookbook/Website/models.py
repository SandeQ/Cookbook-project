from django.db import models
from django import forms
class Recipe(models.Model):
    Title = models.CharField(max_length=64)
    Ingredients = models.CharField(max_length=255)
    Text = models.CharField(max_length=1000)
    Preparation_Time = models.IntegerField()
"""class EditRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['Title', 'Ingredients', 'Text', 'Preparation_Time']"""
# Create your models here.
