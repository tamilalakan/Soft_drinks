# Generated by Django 3.0.5 on 2021-01-05 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_kurupur'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kurupur',
            new_name='Karuppur',
        ),
        migrations.AlterModelOptions(
            name='danishpet',
            options={'verbose_name_plural': 'Danishpet'},
        ),
        migrations.AlterModelOptions(
            name='karuppur',
            options={'verbose_name_plural': 'Kurupur'},
        ),
        migrations.AlterModelOptions(
            name='thenapattai',
            options={'verbose_name_plural': 'Thenapattai'},
        ),
        migrations.AlterModelOptions(
            name='thirupathi',
            options={'verbose_name_plural': 'Thirupathi'},
        ),
    ]
