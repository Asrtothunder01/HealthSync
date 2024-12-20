# Generated by Django 5.0.4 on 2024-11-19 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0002_alter_doctor_user'),
        ('patient', '0002_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_date', models.DateField()),
                ('symptoms', models.TextField()),
                ('Patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
    ]
