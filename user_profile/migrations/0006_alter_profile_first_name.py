# Generated by Django 3.2.3 on 2023-11-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20231118_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='First name'),
        ),
    ]