# Generated by Django 5.1.2 on 2024-10-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akbar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumpstats',
            name='full',
            field=models.BooleanField(),
        ),
    ]
