from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now

from apps.common.models import BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel, RatedModel


positive_validator = MinValueValidator(limit_value=0)


class FoodPortion(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel):
    weight = models.IntegerField('Weight (gr)', default=100, validators=[positive_validator])

    class Meta:
        ordering = ['title']
        verbose_name = 'Food portion'
        verbose_name_plural = 'Food portions'


class FoodCategory(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel):
    class Meta:
        ordering = ['title']
        verbose_name = 'Food category'
        verbose_name_plural = 'Food categories'


class Food(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel, RatedModel):
    category = models.ForeignKey(
        related_name='Category', to=FoodCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    portions = models.ManyToManyField(
        related_name='Portions', to=FoodPortion, blank=True)
    energy = models.IntegerField(
        'Energy (kcal)', default=0, validators=[positive_validator])
    protein = models.DecimalField(
        'Protein (gr)', max_digits=19, decimal_places=4, default=0.0, validators=[positive_validator])
    carbohydrate = models.DecimalField(
        'Carbohydrate (gr)', max_digits=19, decimal_places=4, default=0.0, validators=[positive_validator])
    fat = models.DecimalField(
        'Fat (gr)', max_digits=19, decimal_places=4, default=0.0, validators=[positive_validator])
    fiber = models.DecimalField(
        'Fiber (gr)', max_digits=19, decimal_places=4, default=0.0, validators=[positive_validator])
    sugar = models.DecimalField(
        'Sugar (gr)', max_digits=19, decimal_places=4, default=0.0, validators=[positive_validator])
    salt = models.DecimalField(
        'Salt (gr)', max_digits=19, decimal_places=4, default=0.0, validators=[positive_validator])

    class Meta:
        ordering = ['title']
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class FoodJournal(BaseModel, OwnedModel):
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    weight = models.IntegerField('Weight (gr)', validators=[positive_validator])
    datetime = models.DateTimeField('Datetime', default=now)

    def __str__(self):
        return f'{self.user} {self.food} {self.weight} {self.datetime}'

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Food journal'
        verbose_name_plural = 'Food journal'


class ActivityCategory(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel):
    class Meta:
        ordering = ['title']
        verbose_name = 'Activity category'
        verbose_name_plural = 'Activity categories'


class Activity(BaseModel, TitledModel, DescribedModel, OwnedModel, PublicModel, RatedModel):
    category = models.ForeignKey(
        related_name='Category', to=ActivityCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    energy = models.IntegerField(
        'Energy (kcal/kg/min)', default=0, validators=[positive_validator])

    class Meta:
        ordering = ['title']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'


class ActivityJournal(BaseModel, OwnedModel):
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)
    duration = models.IntegerField('Duration (min)', validators=[positive_validator])
    datetime = models.DateTimeField('Datetime', default=now)

    def __str__(self):
        return f'{self.user} {self.activity} {self.duration} {self.datetime}'

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Activity journal'
        verbose_name_plural = 'Activity journal'
