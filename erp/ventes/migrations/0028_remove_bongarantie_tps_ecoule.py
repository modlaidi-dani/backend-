# Generated by Django 4.2.5 on 2024-12-23 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0027_avoirvente_motif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bongarantie',
            name='tps_ecoule',
        ),
    ]
