# Generated by Django 2.2.24 on 2021-12-26 13:09

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0013_offer_offermap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offerMap',
            field=location_field.models.plain.PlainLocationField(default='41.031964, 29.008841', max_length=63),
        ),
    ]
