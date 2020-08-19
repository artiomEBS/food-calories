from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now

from apps.common.models import BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel, RatedModel


positive_validator = MinValueValidator(limit_value=0)


class FoodPortion(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel):
    weight = models.IntegerField('Weight (gr)', default=100, validators=[positive_validator])

    class Meta:
        verbose_name = 'Food portion'
        verbose_name_plural = 'Food portions'


class FoodCategory(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel):
    uid = models.CharField(default=None, max_length=50, unique=True)

    class Meta:
        verbose_name = 'Food category'
        verbose_name_plural = 'Food categories'


class Food(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel, RatedModel):
    uid = models.CharField(default=None, max_length=50, unique=True)
    category = models.ForeignKey(
        related_name='Category', to=FoodCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    portions = models.ManyToManyField(
        related_name='Portions', to=FoodPortion, blank=True)
    energy = models.IntegerField(
        'Energy (kcal)', default=0, blank=True, null=True, validators=[positive_validator])
    protein = models.FloatField(
        'Protein (gr)', default=0.0, blank=True, null=True, validators=[positive_validator])
    carbohydrate = models.FloatField(
        'Carbohydrate (gr)', default=0.0, blank=True, null=True, validators=[positive_validator])
    fat = models.FloatField(
        'Fat (gr)', default=0.0, blank=True, null=True, validators=[positive_validator])
    fiber = models.FloatField(
        'Fiber (gr)', default=0.0, blank=True, null=True, validators=[positive_validator])
    sugar = models.FloatField(
        'Sugar (gr)', default=0.0, blank=True, null=True, validators=[positive_validator])
    salt = models.FloatField(
        'Salt (gr)', default=0.0, blank=True, null=True, validators=[positive_validator])

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class Activity(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel, RatedModel):
    uid = models.CharField(default=None, max_length=50, unique=True)
    energy = models.FloatField(
        'Energy (kcal/kg/min)', default=0.0, validators=[positive_validator])

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
