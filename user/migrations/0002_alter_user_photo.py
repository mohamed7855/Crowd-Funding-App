# Generated by Django 5.0.1 on 2024-02-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to='user/images'),
        ),
    ]
