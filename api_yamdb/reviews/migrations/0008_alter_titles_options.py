# Generated by Django 3.2 on 2022-12-17 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20221217_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titles',
            options={'ordering': ['name'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]
