from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import *
from django.utils.timezone import now

from apps.common.models import BaseModel


User = get_user_model()


positive_validator = MinValueValidator(limit_value=0)


class TitledModel(BaseModel):
    """ Base model that add title and description """
    title = models.CharField('Title', max_length=128, blank=False, null=False, unique=True)
    description = models.TextField('Description', max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class FoodPortion(TitledModel):
    weight = models.IntegerField('Weight (gr)', default=100, validators=[positive_validator])

    class Meta:
        ordering = ['title']
        verbose_name = 'Food portion'
        verbose_name_plural = 'Food portions'


class FoodCategory(TitledModel):
    portions = models.ManyToManyField(related_name='Portions', to=FoodPortion)

    class Meta:
        ordering = ['title']
        verbose_name = 'Food category'
        verbose_name_plural = 'Food categories'


class Food(TitledModel):
    category = models.ForeignKey(related_name='Category', to=FoodCategory, on_delete=models.CASCADE)
    energy = models.IntegerField('Energy (kcal)', default=0, validators=[positive_validator])
    protein = models.FloatField('Protein (gr)', default=0.0, validators=[positive_validator])
    carbohydrate = models.FloatField('Carbohydrate (gr)', default=0.0, validators=[positive_validator])
    fat = models.FloatField('Fat (gr)', default=0.0, validators=[positive_validator])
    fiber = models.FloatField('Fiber (gr)', default=0.0, validators=[positive_validator])
    sugar = models.FloatField('Sugar (gr)', default=0.0, validators=[positive_validator])
    salt = models.FloatField('Salt (gr)', default=0.0, validators=[positive_validator])

    class Meta:
        ordering = ['title']
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class ActivityCategory(TitledModel):
    class Meta:
        ordering = ['title']
        verbose_name = 'Activity category'
        verbose_name_plural = 'Activity categories'


class Activity(TitledModel):
    category = models.ForeignKey(related_name='Category', to=ActivityCategory, on_delete=models.CASCADE)
    energy = models.IntegerField('Energy (kcal/kg/min)', default=0, validators=[positive_validator])

    class Meta:
        ordering = ['title']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'


class FoodJournal(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    weight = models.IntegerField('Weight (gr)', validators=[positive_validator])
    datetime = models.DateTimeField('Datetime', default=now)

    def __str__(self):
        return f'{self.user} {self.food} {self.weight} {self.datetime}'

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Food journal'
        verbose_name_plural = 'Food journal'


class ActivityJournal(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    activity = models.ForeignKey(to=Activity, on_delete=models.CASCADE)
    duration = models.IntegerField('Duration (min)', validators=[positive_validator])
    datetime = models.DateTimeField('Datetime', default=now)

    def __str__(self):
        return f'{self.user} {self.activity} {self.duration} {self.datetime}'

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Activity journal'
        verbose_name_plural = 'Activity journal'
