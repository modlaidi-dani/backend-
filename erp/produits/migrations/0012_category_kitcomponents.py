# Generated by Django 4.2.5 on 2024-12-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0011_category_kit'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='kitcomponents',
            field=models.TextField(default=''),
        ),
    ]
