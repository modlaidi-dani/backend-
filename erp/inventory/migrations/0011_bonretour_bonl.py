# Generated by Django 4.2.5 on 2024-12-30 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0038_avoirventeancien_bonretour'),
        ('inventory', '0010_remove_bonretour_bonl_remove_bonretour_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonretour',
            name='bonL',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MesbonRetours', to='ventes.bonsortie'),
        ),
    ]
