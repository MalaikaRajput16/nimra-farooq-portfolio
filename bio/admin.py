from django.contrib import admin
from .models import Bio

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    # Use field names from your Bio model
    list_display = ('name', 'job_title')