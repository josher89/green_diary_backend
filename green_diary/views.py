from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import EntrySerializer
from .models import Entry
from django.db.models import Q
from datetime import datetime


class HomeView(TemplateView):
    template_name = "home.html"


class EntryListCreateView(generics.ListCreateAPIView):
    # This is the simplyfied queryset to create each Entry.
    # queryset = Entry.objects.all().order_by("-timestamp")
    serializer_class = EntrySerializer

    def get_queryset(self):
        queryset = Entry.objects.all().order_by("-timestamp")

        # This gets the query parameters
        search_query = self.request.query_params.get("search", None)
        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)
        # New lines/ New month filter and new year filter.
        month = self.request.query_params.get("month", None)
        year = self.request.query_params.get("year", None)

        # This filters by title or content using the search query
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
            # "New line update"
            try:
                search_date = datetime.strptime(search_query, "%Y-%m-%d")
                queryset = queryset.filter(timestamp__date=search_date.date())
            except ValueError:
                pass
        # This filters by the timestamp range
        if start_date:
            try:
                start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
                queryset = queryset.filter(timestamp__gte=start_date_obj)
            except ValueError:
                # This will ignore the invalid date format
                pass

        if end_date:
            try: 
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
                queryset = queryset.filter(timestamp__lte=end_date_obj)
            except ValueError:
                # Again, this will ignore the invalid date format
                pass
        
        # filter by month
        if month:
            try:
                month = int(month) # Ensures month is an interger (1-12)
                queryset = queryset.filter(timestamp__month=month)
            except ValueError:
                pass

        # filter by year
        if year:
            try:
                year = int(year) # Ensures month is an integer
                queryset = queryset.filter(timestamp__year=year)
            except ValueError:
                pass

        return queryset


class EntryDetailView(generics.RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryDeleteView(generics.DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
