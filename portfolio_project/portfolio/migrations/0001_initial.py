# Generated by Django 2.1.1 on 2018-09-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(default=None, max_length=255, unique=True, verbose_name='email address')),
                ('group', models.CharField(default='user', max_length=50)),
                ('last_name', models.CharField(default=None, max_length=150, null=True)),
                ('first_name', models.CharField(default=None, max_length=200, null=True)),
                ('affiliation', models.TextField(default=None, null=True)),
                ('city', models.TextField(default=None, null=True)),
                ('country', models.TextField(default=None, null=True)),
                ('orcid', models.CharField(default=None, max_length=19, null=True)),
                ('last_date_upload', models.DateField(default=None, null=True)),
                ('number_of_upload_this_day', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]