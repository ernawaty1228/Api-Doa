from django.urls import path
from .views import DaftarDoa, DetailDoa

urlpatterns = [
    path('daftar_doa/', DaftarDoa.as_view(), name='daftar_doa'),
    path('detail_doa/<int:pk>/', DetailDoa.as_view(), name='detail_doa'),
]