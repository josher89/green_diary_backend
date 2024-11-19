from django.urls import path
from .views import EntryListCreateView, EntryDeleteView

urlpatterns = [
    path("green_diary/", EntryListCreateView.as_view(), name="entry"),
    path("green_diary/<int:pk>/", EntryDeleteView.as_view(), name="entry-delete"),
]
