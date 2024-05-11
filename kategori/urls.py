from django.urls import path
from .views import DaftarKategori, DetailKategori, DaftarPenulisDoa, DetailPenulisDoa

urlpatterns = [
    path('kategori/', DaftarKategori.as_view(), name='daftar_kategori'),
    path('kategori/<int:pk>/', DetailKategori.as_view(), name='detail_kategori'),
    path('penulis_doa/', DaftarPenulisDoa.as_view(), name='daftar_penulis_doa'),
    path('penulis_doa/<int:pk>/', DetailPenulisDoa.as_view(), name='detail_penulis_doa'),
]
