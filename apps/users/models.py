from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel
from rest_framework_api_key.models import AbstractAPIKey


class UserAPIKey(AbstractAPIKey):
    user = models.ForeignKey(User, related_name='api_keys', on_delete=models.CASCADE)

    class Meta(AbstractAPIKey.Meta):
        verbose_name = "User APIKey"
        verbose_name_plural = "User APIKeys"

    def revoke(self):
        self.revoked = True
        self.save()
        return f"Current APIKey was revoked for the user {self.user.username}."


class Profile(BaseModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


class Target(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    energy = models.IntegerField(null=True, blank=True)
    protein = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    carbohydrate = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    fat = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    fiber = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    salt = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    sugar = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
