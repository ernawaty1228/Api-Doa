from django.db import models
from kategori.models import *

class Doa(models.Model):
    judul_doa = models.CharField(max_length=100)
    teks_doa_latin = models.TextField()
    teks_doa_arab = models.TextField()
    arti_doa = models.TextField()
    tanggal_dibuat = models.DateField(auto_now_add=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    penulis = models.ForeignKey(PenulisDoa, on_delete=models.CASCADE)