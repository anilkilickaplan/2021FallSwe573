# Generated by Django 2.2.24 on 2021-12-09 21:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myclub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('isApproved', models.BooleanField(default=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('createddate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='eventDuration',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='event',
            name='eventTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='offer',
            name='offerDuration',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='offer',
            name='offerTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userFollowers',
            field=models.ManyToManyField(blank=True, related_name='userfollowers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userPicture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventCapacity',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AddField(
            model_name='review',
            name='reviewOffer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myclub.Offer'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offerapplication',
            name='appliedOffer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myclub.Offer'),
        ),
    ]