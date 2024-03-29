# Generated by Django 5.0 on 2024-01-22 17:55

import datetime
import django.db.models.deletion
import django.db.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=50)),
                ('last_name', models.CharField(blank=True, default=None, max_length=50)),
                ('id_number', models.CharField(blank=True, default='', max_length=11, null=True)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2024, 1, 22, 17, 55, 16, 529780, tzinfo=datetime.timezone.utc), null=True)),
                ('sex', models.CharField(default=True)),
                ('telephone', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('blood_group', models.CharField(blank=True, default='', max_length=3, null=True)),
                ('chronic_diseases', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('medical_allergy', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('address_city', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('address_number', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('status', models.CharField(default='Discharge', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProcedureCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField(default=datetime.datetime(2024, 1, 22, 17, 55, 16, 530779, tzinfo=datetime.timezone.utc))),
                ('reasons_for_admission', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('diagnostic_tests', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('diagnosis', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('treatment_plan', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('diagnosis_code', models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='main.diagnosiscode')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2024, 1, 22, 17, 55, 16, 529780, tzinfo=datetime.timezone.utc))),
                ('goal_of_appointment', models.CharField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('number_of_beds', models.CharField(max_length=5)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branch')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalStay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField(blank=True, default=datetime.datetime(2024, 1, 22, 17, 55, 16, 531791, tzinfo=datetime.timezone.utc), null=True)),
                ('discharge_date', models.DateField(blank=True, default=None, null=True)),
                ('medical_procedures', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('additional_info', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
            ],
        ),
    ]
