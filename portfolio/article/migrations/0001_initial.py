# Generated by Django 2.1.7 on 2019-03-27 14:04

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilisateur', '0001_initial'),
        ('categorie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.CharField(default=None, max_length=200)),
                ('titre', models.CharField(default=None, max_length=100)),
                ('content', markdownx.models.MarkdownxField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_projet/')),
                ('categorie_niv1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorie.CategorieNiv1')),
                ('categorie_niv2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorie.CategorieNiv2')),
                ('categorie_niv3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorie.CategorieNiv3')),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.Personne')),
            ],
        ),
    ]
