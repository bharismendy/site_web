# Generated by Django 2.1.7 on 2019-03-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0001_initial'),
        ('article', '0004_auto_20190320_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ManyToManyField(default=None, null=True, to='categorie.Categorie'),
        ),
    ]