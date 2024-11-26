from django.contrib import admin
from .models import Entry

admin.site.register(Entry)
admin.site.site_header = "economiica Admin"
admin.site.site_title = "economiica Admin"
admin.site.index_title = "Welcom to the economiica Admin"
