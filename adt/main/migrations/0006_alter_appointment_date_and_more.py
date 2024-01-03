# Generated by Django 4.2.7 on 2023-12-29 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_unit_name_alter_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 29, 22, 38, 3, 236761, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='admission_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 29, 22, 38, 3, 236761, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='hospitalstay',
            name='admission_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 29, 22, 38, 3, 236761, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 29, 22, 38, 3, 233774, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(blank=True, default='nieznane', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(blank=True, default='nieznane', max_length=50, null=True),
        ),
    ]