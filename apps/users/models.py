from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel


class Profile(BaseModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.IntegerField()
    weight = models.IntegerField()
    date_of_birth = models.DateField()


class Target(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    energy = models.IntegerField()
    protein = models.DecimalField(max_digits=19, decimal_places=4)
    carbohydrate = models.DecimalField(max_digits=19, decimal_places=4)
    fat = models.DecimalField(max_digits=19, decimal_places=4)
    fiber = models.DecimalField(max_digits=19, decimal_places=4)
    salt = models.DecimalField(max_digits=19, decimal_places=4)
    sugar = models.DecimalField(max_digits=19, decimal_places=4)


