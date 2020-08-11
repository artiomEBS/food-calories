from django.contrib import admin

from apps.journal.models import (
    FoodPortion,
    FoodCategory,
    Food,
    ActivityCategory,
    Activity,
    FoodJournal,
    ActivityJournal
)


@admin.register(FoodPortion)
class FoodPortionAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title', 'weight'),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'portions_list', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title', 'portions'),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]

    def portions_list(self, obj):  # noqa
        return ", ".join([portion.title for portion in obj.portions.all()])


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category',
        'energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'sugar', 'salt',
        'date_created', 'date_modified',
    )
    fieldsets = [
        (None, {
            'fields': ('title', 'category'),
        }),
        ('Nutrition', {
            'fields': ('energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'sugar', 'salt')
        }),
        ('Optional', {
            'fields': ('description',)
        }),
    ]


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title',),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(Activity)
class Activity(admin.ModelAdmin):
    list_display = ['title', 'category', 'energy', 'date_created', 'date_modified']
    fieldsets = [
        (None, {
            'fields': ('title', 'category'),
        }),
        ('Nutrition', {
            'fields': ('energy',),
        }),
        ('Optional', {
            'fields': ('description',),
        }),
    ]


@admin.register(FoodJournal)
class FoodJournalAdmin(admin.ModelAdmin):
    list_display = ['user', 'food', 'weight', 'datetime', 'date_created', 'date_modified']
    fields = ['user', 'food', 'weight', 'datetime']


@admin.register(ActivityJournal)
class ActivityJournalAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity', 'duration', 'datetime', 'date_created', 'date_modified']
    fields = ['user', 'activity', 'duration', 'datetime']
