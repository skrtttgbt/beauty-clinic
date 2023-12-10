# Generated by Django 4.0.4 on 2023-10-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_order_createdat_remove_order_updatedat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Pending'), (1, 'Accept'), (2, 'Delete'), (3, 'Decline')], default=0),
        ),
    ]
