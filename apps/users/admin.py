from django.contrib import admin
from apps.users.models import Profile, Target


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'height', 'weight', 'date_of_birth')


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('user', 'energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'salt', 'sugar')
