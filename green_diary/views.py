# from django.shortcuts import render
from rest_framework import generics
from .serializers import EntrySerializer
from .models import Entry


class EntryListCreateView(generics.ListCreateAPIView):
    queryset = Entry.objects.all().order_by("-timestamp")
    serializer_class = EntrySerializer


class EntryDeleteView(generics.DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
