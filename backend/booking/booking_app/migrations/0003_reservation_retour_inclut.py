# Generated by Django 4.1.1 on 2022-09-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_vol_places_alter_reservation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='retour_inclut',
            field=models.BooleanField(default=False),
        ),
    ]