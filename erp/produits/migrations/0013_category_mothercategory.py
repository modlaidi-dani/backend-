# Generated by Django 4.2.5 on 2024-12-25 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0012_category_kitcomponents'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='MotherCategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variants', to='produits.category'),
        ),
    ]
