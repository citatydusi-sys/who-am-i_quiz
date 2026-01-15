from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Category(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    english = models.CharField(max_length=100)
    kazakh = models.CharField(max_length=100)