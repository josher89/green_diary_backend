from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import EntrySerializer
from .models import Entry


class HomeView(TemplateView):
    template_name = "home.html"


class EntryListCreateView(generics.ListCreateAPIView):
    queryset = Entry.objects.all().order_by("-timestamp")
    serializer_class = EntrySerializer


class EntryDeleteView(generics.DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
