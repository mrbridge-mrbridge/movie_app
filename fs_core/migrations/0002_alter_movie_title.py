# Generated by Django 4.0.3 on 2022-03-15 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
