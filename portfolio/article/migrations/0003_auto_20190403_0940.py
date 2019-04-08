# Generated by Django 2.1.7 on 2019-04-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190402_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie_niv2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorie.CategorieNiv2'),
        ),
        migrations.AlterField(
            model_name='article',
            name='categorie_niv3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorie.CategorieNiv3'),
        ),
    ]