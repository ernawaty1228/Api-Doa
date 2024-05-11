from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Kategori, PenulisDoa
from .serializers import KategoriSerializer, PenulisDoaSerializer

# Views untuk Kategori
class DaftarKategori(APIView):
    def get(self, request):
        kategori = Kategori.objects.all()
        serializer = KategoriSerializer(kategori, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailKategori(APIView):
    def get_object(self, pk):
        try:
            return Kategori.objects.get(pk=pk)
        except Kategori.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        kategori = self.get_object(pk)
        serializer = KategoriSerializer(kategori)
        return Response(serializer.data)

    def put(self, request, pk):
        kategori = self.get_object(pk)
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        kategori = self.get_object(pk)
        kategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views untuk Penulis Doa
class DaftarPenulisDoa(APIView):
    def get(self, request):
        penulis_doa = PenulisDoa.objects.all()
        serializer = PenulisDoaSerializer(penulis_doa, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PenulisDoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailPenulisDoa(APIView):
    def get_object(self, pk):
        try:
            return PenulisDoa.objects.get(pk=pk)
        except PenulisDoa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        penulis_doa = self.get_object(pk)
        serializer = PenulisDoaSerializer(penulis_doa)
        return Response(serializer.data)

    def put(self, request, pk):
        penulis_doa = self.get_object(pk)
        serializer = PenulisDoaSerializer(penulis_doa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        penulis_doa = self.get_object(pk)
        penulis_doa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
