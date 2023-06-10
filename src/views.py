from django.shortcuts import render

from rest_framework import viewsets

from .models import article

from .serializers import articleserializer

# Create your views here.

class articleviewset(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = articleserializer