# Generated by Django 3.0.5 on 2021-01-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danishpet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('address', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
