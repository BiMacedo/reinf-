# Generated by Django 4.2.2 on 2023-06-27 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='usuarios',
        ),
    ]