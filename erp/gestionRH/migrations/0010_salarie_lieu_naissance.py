# Generated by Django 4.2.5 on 2025-01-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionRH', '0009_salarie_fonctionarabe'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarie',
            name='lieu_naissance',
            field=models.CharField(default='', max_length=255),
        ),
    ]
