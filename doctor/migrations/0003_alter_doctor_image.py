# Generated by Django 4.2.4 on 2023-09-01 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_email_remove_doctor_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/doctors'),
        ),
    ]
