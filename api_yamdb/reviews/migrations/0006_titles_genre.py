# Generated by Django 3.2 on 2022-12-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_genrestitles_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(through='reviews.GenresTitles', to='reviews.Genres'),
        ),
    ]