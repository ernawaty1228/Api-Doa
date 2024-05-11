from rest_framework import serializers
from .models import Doa

class DoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doa
        fields = ['id', 'judul_doa', 'teks_doa_latin', 'teks_doa_arab', 'arti_doa', 'tanggal_dibuat', 'kategori', 'penulis']
