from django.shortcuts import render
from rest_framework import generics
from .models import Kasir
from .serializers import KasirSerializer


class KasirListCreate(generics.ListCreateAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer


