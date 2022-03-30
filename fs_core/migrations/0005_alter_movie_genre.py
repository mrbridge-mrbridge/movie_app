# Generated by Django 4.0.3 on 2022-03-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs_core', '0004_alter_movie_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Fiction', 'Fiction'), ('Romance', 'Romance'), ('Documentary', 'Documentary'), ('Animation', 'Animation'), ('Fantasy', 'Fantasy'), ('Sports', 'Sports'), ('Spirituality', 'Spirituality')], max_length=50),
        ),
    ]
