# Generated by Django 2.2.24 on 2021-12-24 22:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0011_event_eventcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventCapacity',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
