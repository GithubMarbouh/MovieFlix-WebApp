# Generated by Django 4.2 on 2023-04-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_cast_movielinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]