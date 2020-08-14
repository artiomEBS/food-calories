from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()

positive_validator = MinValueValidator(limit_value=0)


# Base class date_created and date_modified
class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TitledModel(models.Model):
    title = models.CharField('Title', max_length=128, blank=False, null=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class DescribedModel(models.Model):
    description = models.TextField('Description', max_length=1024, blank=True, null=True)

    class Meta:
        abstract = True


class OwnedModel(models.Model):
    user = models.ForeignKey(to=User, null=True, blank=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class PublicModel(models.Model):
    is_public = models.BooleanField('Is public', default=False)

    class Meta:
        abstract = True


class RatedModel(models.Model):
    rating = models.IntegerField('Rating', default=0, validators=[positive_validator])

    class Meta:
        abstract = True
