# Generated by Django 4.2.5 on 2024-12-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_stock_quantity_blocked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='quantity_initial',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
