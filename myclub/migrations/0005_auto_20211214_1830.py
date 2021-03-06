# Generated by Django 2.2.24 on 2021-12-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0004_userprofile_userreservehour'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventPicture',
            field=models.ImageField(blank=True, default='uploads/event_pictures/default.png', upload_to='uploads/event_pictures/'),
        ),
        migrations.AddField(
            model_name='offer',
            name='offerPicture',
            field=models.ImageField(blank=True, default='uploads/offer_pictures/default.png', upload_to='uploads/offer_pictures/'),
        ),
    ]
