# Generated by Django 3.2.3 on 2024-01-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20240105_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
