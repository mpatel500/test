from django.db import models

class Webserver(models.Model):
    name = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    patch_level = models.CharField(max_length=50)
    in_use = models.BooleanField(default=False)

class Database(models.Model):
    name = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    patch_level = models.CharField(max_length=50)
    in_use = models.BooleanField(default=False)

class Host(models.Model):
    fqdn = models.CharField(max_length=100)
    os_type = models.CharField(max_length=50)
    os_patch_level = models.CharField(max_length=50)
    environment = models.CharField(max_length=50)
