# Generated by Django 2.2.24 on 2021-12-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0005_auto_20211214_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userSurname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
