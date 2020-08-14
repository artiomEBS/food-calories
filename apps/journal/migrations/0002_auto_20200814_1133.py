# Generated by Django 3.1 on 2020-08-14 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='activitycategory',
            options={'verbose_name': 'Activity category', 'verbose_name_plural': 'Activity categories'},
        ),
        migrations.AlterModelOptions(
            name='activityjournal',
            options={'verbose_name': 'Activity journal', 'verbose_name_plural': 'Activity journal'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterModelOptions(
            name='foodcategory',
            options={'verbose_name': 'Food category', 'verbose_name_plural': 'Food categories'},
        ),
        migrations.AlterModelOptions(
            name='foodjournal',
            options={'verbose_name': 'Food journal', 'verbose_name_plural': 'Food journal'},
        ),
        migrations.AlterModelOptions(
            name='foodportion',
            options={'verbose_name': 'Food portion', 'verbose_name_plural': 'Food portions'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Category', to='journal.activitycategory'),
        ),
    ]
