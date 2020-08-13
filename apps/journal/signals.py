from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from apps.journal import models


@receiver(pre_save, sender=models.FoodJournal)
def good_increment_rating(sender, **kwargs):
    print(sender)


@receiver(post_delete, sender=models.FoodJournal)
def food_decrement_rating(sender, **kwargs):
    print(sender)


@receiver(pre_save, sender=models.ActivityJournal)
def activity_increment_rating(sender, **kwargs):
    print(sender)


@receiver(post_delete, sender=models.ActivityJournal)
def activity_decrement_rating(sender, **kwargs):
    print(sender)
