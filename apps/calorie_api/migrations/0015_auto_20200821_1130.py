# Generated by Django 3.1 on 2020-08-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_api', '0014_auto_20200819_0954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='foodcategory',
            options={'verbose_name': 'Food category', 'verbose_name_plural': 'Food categories'},
        ),
        migrations.AlterModelOptions(
            name='foodportion',
            options={'verbose_name': 'Food portion', 'verbose_name_plural': 'Food portions'},
        ),
    ]
