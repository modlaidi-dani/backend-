# Generated by Django 4.2.5 on 2024-12-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_bonretour_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonretour',
            name='valide',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
