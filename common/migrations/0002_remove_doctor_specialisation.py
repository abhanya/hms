# Generated by Django 4.1.7 on 2023-03-24 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='specialisation',
        ),
    ]
