# Generated by Django 4.2.5 on 2025-01-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionRH', '0004_salarie_association'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarie',
            name='ccp',
            field=models.CharField(default='', max_length=255),
        ),
    ]
