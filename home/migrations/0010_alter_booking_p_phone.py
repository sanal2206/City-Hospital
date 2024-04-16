# Generated by Django 4.2.6 on 2024-04-11 06:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_booking_p_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='p_phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Enter a valid phone number with exactly 10 digits', regex='^\\d{10}$')]),
        ),
    ]
