# Generated by Django 5.0.1 on 2024-02-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('confirmPass', models.TextField()),
                ('mobilPhone', models.TextField()),
                ('photo', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
