# Generated by Django 5.0.4 on 2024-04-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_contactmessage_addeddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='addedDate',
            field=models.DateField(auto_now_add=True, verbose_name='Date this was sent'),
        ),
    ]