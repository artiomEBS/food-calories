from django.contrib import admin
from apps.journal import models


@admin.register(models.FoodPortion)
class FoodPortionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'weight', 'user', 'is_public', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title', 'weight',),
        }),
        ('Published', {
            'fields': ('user', 'is_public'),
        }),
        ('Optional', {
            'fields': ('description',),
        }),
    ]


@admin.register(models.FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_public', 'date_created', 'date_modified')
    fieldsets = [
        (None, {
            'fields': ('title',),
        }),
        ('Published', {
            'fields': ('user', 'is_public'),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'category', 'user', 'is_public', 'rating',
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
            'fields': ('user', 'is_public',),
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
    list_display = ['id', 'food', 'weight', 'datetime', 'user', 'date_created', 'date_modified']
    fields = ['food', 'weight', 'datetime', 'user']


@admin.register(models.ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_public', 'date_created', 'date_modified',)
    fieldsets = [
        (None, {
            'fields': ('title',),
        }),
        ('Published', {
            'fields': ('user', 'is_public',),
        }),
        ('Optional', {
            'fields': ('description',),
        })
    ]


@admin.register(models.Activity)
class Activity(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'energy', 'user', 'is_public', 'date_created', 'date_modified']
    fieldsets = [
        (None, {
            'fields': ('title', 'category',),
        }),
        ('Nutrition', {
            'fields': ('energy',),
        }),
        ('Published', {
            'fields': ('user', 'is_public',),
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
    list_display = ['id', 'activity', 'duration', 'datetime', 'user', 'date_created', 'date_modified']
    fields = ['activity', 'duration', 'datetime', 'user']
