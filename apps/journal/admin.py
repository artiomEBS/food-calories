from django.contrib import admin
from apps.journal import models


@admin.register(models.FoodJournal)
class FoodJournalAdmin(admin.ModelAdmin):
    list_display = ['id', 'food', 'weight', 'datetime', 'user', 'date_created', 'date_modified']
    fields = ['food', 'weight', 'datetime', 'user']


@admin.register(models.ActivityJournal)
class ActivityJournalAdmin(admin.ModelAdmin):
    list_display = ['id', 'activity', 'duration', 'datetime', 'user', 'date_created', 'date_modified']
    fields = ['activity', 'duration', 'datetime', 'user']
