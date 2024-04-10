# Generated by Django 5.0.4 on 2024-04-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_row_id_row_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='row',
            name='index',
        ),
        migrations.AddField(
            model_name='row',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
