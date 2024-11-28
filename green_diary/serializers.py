from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        # "This specify the fields to include"
        fields = ["id", "title", "text", "timestamp"]
