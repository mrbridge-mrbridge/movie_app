# Generated by Django 4.0.3 on 2022-03-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs_core', '0003_movie_status_movie_views_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(blank=True, choices=[('Most Watched', 'Most Watched'), ('Top Rated', 'Top Rated'), ('Recently Added', 'Recently Added')], max_length=50, null=True),
        ),
    ]
