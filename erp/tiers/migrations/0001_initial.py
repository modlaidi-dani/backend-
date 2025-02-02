# Generated by Django 4.2.5 on 2024-12-22 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('adresse', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('bic', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('adresse', models.CharField(default='', max_length=250)),
                ('phone', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('sourceClient', models.CharField(default='', max_length=150)),
                ('registreCommerce', models.CharField(default='', max_length=150)),
                ('Nif', models.CharField(default='', max_length=150)),
                ('Nis', models.CharField(default='', max_length=150)),
                ('num_article', models.CharField(default='', max_length=150)),
                ('region_client', models.CharField(default='', max_length=150)),
                ('solde', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('valide', models.BooleanField(default=True)),
                ('NisDoc', models.FileField(upload_to='media/document')),
                ('NifDoc', models.FileField(upload_to='media/document')),
                ('RCDoc', models.FileField(upload_to='media/document')),
                ('AIDoc', models.FileField(upload_to='media/document')),
            ],
        ),
        migrations.CreateModel(
            name='CompteBancaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelCompte', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('TypeCompte', models.TextField(blank=True, null=True)),
                ('compteclient', models.TextField(blank=True, null=True)),
                ('num_compte', models.IntegerField(blank=True, null=True)),
                ('cle', models.IntegerField(blank=True, null=True)),
                ('IBAN', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeFournisseur', models.CharField(max_length=25)),
                ('acronym', models.CharField(max_length=150)),
                ('raison_Social', models.CharField(max_length=150)),
                ('adresse', models.CharField(default='', max_length=250)),
                ('phone', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('typefournisseur', models.CharField(choices=[('PME', 'PME'), ('Institutionnel', 'Institutionnel'), ('Automobile', 'Automobile'), ('Revendeur', 'Revendeur'), ('BTPH', 'BTPH'), ('Industrie', 'Industrie'), ('Autre', 'Autre')], default='Autre', max_length=25)),
                ('fournisseurEtrange', models.BooleanField()),
                ('fournisseurClient', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ProspectionClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SourceClient', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('etatProspection', models.CharField(blank=True, default='', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('wilayas', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tentatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebutTentative', models.DateTimeField()),
                ('dateFinTentative', models.DateTimeField()),
                ('MoyenContact', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('propspection', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_tentative', to='tiers.prospectionclient')),
            ],
        ),
    ]
