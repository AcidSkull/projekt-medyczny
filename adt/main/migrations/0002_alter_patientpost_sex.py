# Generated by Django 4.2.7 on 2023-12-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientpost',
            name='sex',
            field=models.CharField(choices=[(True, 'Male'), (False, 'Female')]),
        ),
    ]