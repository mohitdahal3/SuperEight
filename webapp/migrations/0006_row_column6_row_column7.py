# Generated by Django 5.0.4 on 2024-04-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_row_column10_remove_row_column6_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='column6',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='row',
            name='column7',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
