from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

class PenulisDoa(models.Model):
    nama_penulis = models.CharField(max_length=100)
