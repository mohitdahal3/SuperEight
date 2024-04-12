# Generated by Django 5.0.4 on 2024-04-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_row_column6_row_column7'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('message', models.TextField(max_length=2000)),
                ('addedDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]