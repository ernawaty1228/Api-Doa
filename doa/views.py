from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doa
from .serializers import DoaSerializer
from django.http import Http404

class DaftarDoa(APIView):
    def get(self, request):
        doa = Doa.objects.all()
        serializer = DoaSerializer(doa, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailDoa(APIView):
    def get_object(self, pk):
        try:
            return Doa.objects.get(pk=pk)
        except Doa.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        doa = self.get_object(pk)
        serializer = DoaSerializer(doa)
        return Response(serializer.data)

    def put(self, request, pk):
        doa = self.get_object(pk)
        serializer = DoaSerializer(doa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doa = self.get_object(pk)
        doa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
