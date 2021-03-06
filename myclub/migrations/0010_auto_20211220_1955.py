# Generated by Django 2.2.24 on 2021-12-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0009_auto_20211219_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offerCategory',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerPicture',
            field=models.ImageField(blank=True, default='uploads/offer_pictures/default.png', upload_to='uploads/offer_pictures/'),
        ),
    ]
