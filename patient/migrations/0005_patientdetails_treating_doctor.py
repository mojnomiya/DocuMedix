# Generated by Django 4.2.4 on 2023-09-01 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_remove_doctor_patients'),
        ('patient', '0004_patientdetails_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='treating_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctor'),
        ),
    ]
