# Generated by Django 3.2.7 on 2021-09-11 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_patient_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='hospital',
        ),
    ]
