from django.db import models


class Entry(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.timestamp}"
