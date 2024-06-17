from django.db import models


class Info(models.Model):
    info_icon = models.CharField(max_length=50)
    info_text = models.TextField()

# Create your models here.
