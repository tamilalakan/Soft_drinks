# Generated by Django 3.0.5 on 2021-01-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=10, null=True),
        ),
    ]