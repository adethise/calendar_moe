from django.contrib import admin
from .models import DateEntry, Date

@admin.register(DateEntry)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    pass
