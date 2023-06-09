# Generated by Django 4.1.7 on 2023-03-24 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('discription_date', models.DateField(auto_now=True)),
                ('Booking', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='patient.booking')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.doctor')),
                ('patient', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='common.patient')),
            ],
        ),
    ]
