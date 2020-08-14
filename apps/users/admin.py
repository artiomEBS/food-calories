from django.contrib import admin
from apps.users.models import UserAPIKey, Profile, Target
from rest_framework_api_key.admin import APIKeyModelAdmin


@admin.register(UserAPIKey)
class UserAPIkeyAdmin(APIKeyModelAdmin):
    list_display = ('user', "prefix", "name", "created", "expiry_date", "_has_expired", "revoked",)
    search_fields = ('user__username', 'prefix', 'name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'height', 'weight', 'date_of_birth',)
    search_fields = ('id', 'user__username', 'gender', 'height', 'weight',)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'energy', 'protein', 'carbohydrate', 'fat', 'fiber', 'salt', 'sugar',)
    search_fields = ('id', 'user__username',)
