# Generated by Django 2.1.7 on 2019-04-15 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(default=None, max_length=100, unique=True)),
                ('has_sub', models.BooleanField(default=False)),
                ('niv_cat', models.IntegerField(choices=[(3, 3), (4, 4), (1, 1), (2, 2)], default=None, null=True)),
                ('cat_sup', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorie.Categorie')),
            ],
        ),
    ]
