# Generated by Django 4.2.6 on 2023-11-25 16:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_booking_p_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='p_phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits and contain only numeric characters.', regex='^\\d{10}$'), django.core.validators.MinLengthValidator(limit_value=10, message='Phone number must be at least 10 digits.'), django.core.validators.MaxLengthValidator(limit_value=10, message='Phone number cannot exceed 10 digits.')]),
        ),
    ]
