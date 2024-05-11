from rest_framework import serializers
from .models import Kategori, PenulisDoa

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama_kategori']

class PenulisDoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenulisDoa
        fields = ['id', 'nama_penulis']