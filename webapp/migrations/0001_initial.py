# Generated by Django 5.0.4 on 2024-04-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isHeading', models.BooleanField()),
                ('column1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column7', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column8', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column9', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('column10', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
    ]
