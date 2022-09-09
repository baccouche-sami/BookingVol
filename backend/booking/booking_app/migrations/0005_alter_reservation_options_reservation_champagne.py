# Generated by Django 4.1.1 on 2022-09-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0004_alter_reservation_options_remove_reservation_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['id', 'vol', 'user', 'montant', 'champagne', 'date_depart', 'date_retour'], 'verbose_name': 'Reservation'},
        ),
        migrations.AddField(
            model_name='reservation',
            name='champagne',
            field=models.BooleanField(default=False),
        ),
    ]
