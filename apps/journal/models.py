from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.utils.timezone import now

from apps.calorie_api.models import Activity, Food
from apps.common.models import BaseModel


User = get_user_model()
positive_validator = MinValueValidator(limit_value=0)


class FoodJournal(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    weight = models.IntegerField('Weight (gr)', validators=[positive_validator])
    datetime = models.DateTimeField('Datetime', default=now)

    def __str__(self):
        return f'{self.user} {self.food} {self.weight} {self.datetime}'

    class Meta:
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
