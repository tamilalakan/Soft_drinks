# Generated by Django 3.0.5 on 2021-01-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_employee_daily_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='daily_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
