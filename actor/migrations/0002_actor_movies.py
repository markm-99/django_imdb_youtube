# Generated by Django 3.1 on 2020-09-04 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_auto_20200904_1722'),
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(to='movie.Movie'),
        ),
    ]
