# Generated by Django 5.0.1 on 2024-02-19 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundProject', '0002_remove_rate_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
    ]
