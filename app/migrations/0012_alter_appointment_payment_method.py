# Generated by Django 4.0.4 on 2023-10-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_order_product_service_remove_appointment_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='payment_method',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Cash'), (2, 'Gcash'), (3, 'Card')], default=1),
        ),
    ]
