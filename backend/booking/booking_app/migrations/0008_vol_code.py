# Generated by Django 4.1.1 on 2022-09-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0007_alter_reservation_options_remove_reservation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vol',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
