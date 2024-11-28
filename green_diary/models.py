from django.db import models


class Entry(models.Model):
    # "For the searchable title"
    title = models.CharField(max_length=225, default="untitled", blank=True)
    # "For the diary content"
    text = models.TextField()
    # "For filtering by time"
    timestamp = models.DateTimeField(auto_now_add=True)

    # "Old code"
    # def __str__(self):
    #     return f"{self.text} - {self.timestamp}"

    def __str__(self):
        return self.title
