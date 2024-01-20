# Generated by Django 3.2.3 on 2024-01-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_post_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tagline',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
    ]
