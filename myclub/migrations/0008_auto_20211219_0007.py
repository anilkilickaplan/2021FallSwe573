# Generated by Django 2.2.24 on 2021-12-19 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0007_auto_20211215_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userSurname',
            new_name='userNameSurname',
        ),
    ]