# Generated by Django 4.1.1 on 2022-09-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booking_app", "0006_alter_reservation_options_reservation_nb_place_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reservation",
            options={
                "ordering": [
                    "id",
                    "nom",
                    "prenom",
                    "nb_place",
                    "vol",
                    "montant",
                    "champagne",
                    "date_depart",
                    "date_retour",
                ],
                "verbose_name": "Reservation",
            },
        ),
        migrations.RemoveField(model_name="reservation", name="user",),
    ]
