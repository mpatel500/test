from django.db import models

class Webserver(models.Model):
    name = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    patch_level = models.CharField(max_length=50)
