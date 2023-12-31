# Generated by Django 4.0.4 on 2023-03-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_appointment_age_appointment_date_of_death_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='deceased_full_name',
            field=models.CharField(blank=True, default='', help_text='Surname FirstName, MiddleName', max_length=50, null=True, verbose_name='Deceased Full Name'),
        ),
    ]
