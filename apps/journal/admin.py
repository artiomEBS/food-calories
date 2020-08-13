from django.contrib import admin
from apps.journal import models


@admin.register(models.FoodPortion)
class FoodPortionAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'owner', 'is_public', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title', 'weight',),
        }),
        ('Published', {
            'fields': ('owner', 'is_public'),
        }),
        ('Optional', {
            'fields': ('description',),
        }),
    ]


@admin.register(models.FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_public', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title',),
        }),
        ('Published', {
            'fields': ('owner', 'is_public'),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'owner', 'is_public', 'rating',
        'energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'sugar', 'salt',
        'date_created', 'date_modified',
    )
    fieldsets = [
        (None, {
            'fields': ('title', 'category', 'portions',),
        }),
        ('Nutrition', {
            'fields': ('energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'sugar', 'salt',)
        }),
        ('Published', {
            'fields': ('owner', 'is_public',),
        }),
        ('Rating', {
            'fields': ('rating',),
        }),
        ('Optional', {
            'fields': ('description',)
        }),
    ]


@admin.register(models.FoodJournal)
class FoodJournalAdmin(admin.ModelAdmin):
    list_display = ['food', 'weight', 'datetime', 'owner', 'date_created', 'date_modified']
    fields = ['food', 'weight', 'datetime', 'owner']


@admin.register(models.ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_public', 'date_created', 'date_modified',)
    fieldsets = [
        (None, {
            'fields': ('title',),
        }),
        ('Published', {
            'fields': ('owner', 'is_public',),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(models.Activity)
class Activity(admin.ModelAdmin):
    list_display = ['title', 'category', 'energy', 'owner', 'is_public', 'date_created', 'date_modified']
    fieldsets = [
        (None, {
            'fields': ('title', 'category',),
        }),
        ('Nutrition', {
            'fields': ('energy',),
        }),
        ('Published', {
            'fields': ('owner', 'is_public',),
        }),
        ('Rating', {
            'fields': ('rating',),
        }),
        ('Optional', {
            'fields': ('description',),
        }),
    ]


@admin.register(models.ActivityJournal)
class ActivityJournalAdmin(admin.ModelAdmin):
    list_display = ['activity', 'duration', 'datetime', 'owner', 'date_created', 'date_modified']
    fields = ['activity', 'duration', 'datetime', 'owner']
