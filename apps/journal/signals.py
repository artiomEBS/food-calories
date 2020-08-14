from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from apps.journal import models


@receiver(post_save, sender=models.FoodJournal)
def food_increment_rating(sender, instance, **kwargs):
    instance.food.rating += 1
    instance.food.save()


@receiver(pre_delete, sender=models.FoodJournal)
def food_decrement_rating(sender, instance, **kwargs):
    instance.food.rating -= 1
    instance.food.save()


@receiver(post_save, sender=models.ActivityJournal)
def activity_increment_rating(sender, instance, **kwargs):
    instance.activity.rating += 1
    instance.activity.save()


@receiver(pre_delete, sender=models.ActivityJournal)
def activity_decrement_rating(sender, instance, **kwargs):
    instance.activity.rating -= 1
    instance.activity.save()
