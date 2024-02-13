from django.db import models

class Categories(models.Model):
    categoryName = models.CharField(max_length=20)