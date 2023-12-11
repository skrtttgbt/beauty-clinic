# Generated by Django 4.0.4 on 2023-08-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_appointment_death_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status_description',
            field=models.TextField(default='Your appointment is not yet approved, just wait a few hours before getting approved, thank you.', help_text='Describe the reason for changing the status', max_length=255),
        ),
    ]