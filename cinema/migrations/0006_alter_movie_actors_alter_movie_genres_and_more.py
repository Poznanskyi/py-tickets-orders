# Generated by Django 4.1 on 2024-10-03 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0005_alter_movie_actors_alter_movie_genres_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(to="cinema.actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="cinema.genre"),
        ),
        migrations.AlterField(
            model_name="moviesession",
            name="cinema_hall",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cinema.cinemahall"
            ),
        ),
        migrations.AlterField(
            model_name="moviesession",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cinema.movie"
            ),
        ),
    ]
