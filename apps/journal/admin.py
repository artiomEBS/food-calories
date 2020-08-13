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
    list_display = ('title', 'weight', 'owner', 'is_public', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title', 'weight', 'owner', 'is_public'),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'portions_list', 'owner', 'is_public', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title', 'portions', 'owner', 'is_public'),
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
        'title', 'category', 'owner', 'is_public', 'rating',
        'energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'sugar', 'salt',
        'date_created', 'date_modified',
    )
    fieldsets = [
        (None, {
            'fields': ('title', 'category', 'owner', 'is_public', 'rating'),
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
    list_display = ('title', 'owner', 'is_public', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title', 'owner', 'is_public'),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(Activity)
class Activity(admin.ModelAdmin):
    list_display = ['title', 'category', 'energy', 'owner', 'is_public', 'date_created', 'date_modified']
    fieldsets = [
        (None, {
            'fields': ('title', 'category', 'owner', 'is_public'),
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
    list_display = ['food', 'weight', 'datetime', 'owner', 'date_created', 'date_modified']
    fields = ['food', 'weight', 'datetime', 'owner']


@admin.register(ActivityJournal)
class ActivityJournalAdmin(admin.ModelAdmin):
    list_display = ['activity', 'duration', 'datetime', 'owner', 'date_created', 'date_modified']
    fields = ['activity', 'duration', 'datetime', 'owner']
