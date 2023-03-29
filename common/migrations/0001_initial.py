# Generated by Django 4.1.7 on 2023-03-24 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_name', models.CharField(max_length=20)),
                ('pat_email', models.CharField(max_length=60)),
                ('pat_address', models.CharField(max_length=50)),
                ('pat_gender', models.CharField(max_length=50)),
                ('pat_phone', models.BigIntegerField()),
                ('pat_pass', models.CharField(max_length=8)),
                ('age', models.IntegerField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=20)),
                ('doc_email', models.CharField(max_length=60)),
                ('doc_address', models.CharField(max_length=50)),
                ('doc_gender', models.CharField(max_length=50)),
                ('doc_phone', models.BigIntegerField()),
                ('doc_pass', models.CharField(max_length=8)),
                ('doc_dob', models.DateField(auto_now=True)),
                ('doc_username', models.CharField(max_length=50)),
                ('specialisation', models.CharField(max_length=100)),
                ('doc_state', models.CharField(max_length=100)),
                ('approve', models.BooleanField(default=False)),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='projectadmin.department')),
            ],
        ),
    ]