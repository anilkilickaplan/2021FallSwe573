# Generated by Django 2.2.24 on 2021-12-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0017_auto_20211231_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='is_given',
            field=models.BooleanField(default=False),
        ),
    ]
