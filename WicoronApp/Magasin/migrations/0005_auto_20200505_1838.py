# Generated by Django 3.0.3 on 2020-05-05 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Magasin', '0004_remove_panier_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commande_has_Produits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Magasin.Commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Magasin.Produit')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='Produits',
            field=models.ManyToManyField(default=None, through='Magasin.Commande_has_Produits', to='Magasin.Produit'),
        ),
    ]
