# Generated by Django 4.2.5 on 2024-12-22 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientInfo', '0001_initial'),
        ('achats', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClotureReglements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('date', models.DateField()),
                ('collected', models.BooleanField(default=False)),
                ('montant_collected', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='depense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EcheanceReglement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriqueMontantRecuperer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ModeReglement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('actif', models.BooleanField(default=True)),
                ('num_cheque', models.CharField(blank=True, default='', max_length=2500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='montantCollected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='mouvementCaisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('debit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('motif', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reglement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeReglement', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('type_reglement', models.CharField(choices=[('paiement', 'paiement'), ('remboursement', 'remboursement')], max_length=100)),
                ('collected', models.BooleanField(default=False)),
                ('dateReglement', models.DateField()),
                ('num_cheque', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('note', models.TextField(blank=True, default='', null=True)),
                ('piece_jointe', models.FileField(blank=True, null=True, upload_to='pj')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDepense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('salaire', 'Salaire'), ('loyer', 'Loyer'), ('divers', 'Divers')], max_length=20)),
                ('nom_salarie', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('fonction_salarie', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('adresse_salarie', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('tlfn_salarie', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('numero_local', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('adresse_local', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('designation', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientInfo.store')),
            ],
        ),
        migrations.CreateModel(
            name='ReglementFournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeReglement', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('type_reglement', models.CharField(choices=[('paiement', 'paiement'), ('remboursement', 'remboursement')], max_length=100)),
                ('collected', models.BooleanField(default=False)),
                ('dateReglement', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=15)),
                ('BonA', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bonAchats_reglements', to='achats.bonachat')),
                ('CompteEntreprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fournisseurs_reglements', to='clientInfo.compteentreprise')),
                ('facture', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='factureAchats_reglements', to='achats.factureachat')),
            ],
        ),
    ]
