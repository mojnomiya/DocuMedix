# Generated by Django 4.2.4 on 2023-09-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_patientdetails_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='department',
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='first_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='last_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
