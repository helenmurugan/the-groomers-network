# Generated by Django 3.2.23 on 2023-11-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]