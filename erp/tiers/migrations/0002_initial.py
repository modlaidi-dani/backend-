# Generated by Django 4.2.5 on 2024-12-22 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('clientInfo', '0002_initial'),
        ('tiers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tentatives',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_tentatives', to='user.customuser'),
        ),
        migrations.AddField(
            model_name='region',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_regions', to='clientInfo.store'),
        ),
        migrations.AddField(
            model_name='prospectionclient',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ma_prospection', to='tiers.client'),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='store',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fournisseur_store', to='clientInfo.store'),
        ),
        migrations.AddField(
            model_name='comptebancaire',
            name='Agence',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compte_banque_client', to='tiers.agence'),
        ),
        migrations.AddField(
            model_name='comptebancaire',
            name='Banque',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compte_banque_client', to='tiers.banque'),
        ),
        migrations.AddField(
            model_name='comptebancaire',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compte_bancaire_client', to='tiers.client'),
        ),
        migrations.AddField(
            model_name='comptebancaire',
            name='fournisseur',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compte_bancaire_client', to='tiers.fournisseur'),
        ),
        migrations.AddField(
            model_name='client',
            name='categorie_client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_type', to='clientInfo.typeclient'),
        ),
        migrations.AddField(
            model_name='client',
            name='store',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_store', to='clientInfo.store'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_clients', to='user.customuser'),
        ),
        migrations.AddField(
            model_name='banque',
            name='store',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banque_store', to='clientInfo.store'),
        ),
        migrations.AddField(
            model_name='agence',
            name='banque',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banque_agence', to='tiers.banque'),
        ),
        migrations.AddField(
            model_name='agence',
            name='store',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agence_store', to='clientInfo.store'),
        ),
    ]
