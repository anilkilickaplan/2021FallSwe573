# Generated by Django 2.2.24 on 2021-12-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0010_auto_20211220_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventCategory',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
