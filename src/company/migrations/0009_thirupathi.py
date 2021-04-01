# Generated by Django 3.0.5 on 2021-01-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_delete_thirupathi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thirupathi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('address', models.TextField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Thirupathi',
            },
        ),
    ]
