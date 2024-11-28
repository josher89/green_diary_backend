from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp',]
    search_fields = ['title', 'text',]
    list_filter = ['timestamp',]

admin.site.site_header = "economiica Admin"
admin.site.site_title = "economiica Admin"
admin.site.index_title = "Welcom to the economiica Admin"
