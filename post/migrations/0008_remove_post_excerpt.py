# Generated by Django 3.2.3 on 2024-01-07 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
    ]