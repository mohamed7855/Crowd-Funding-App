# Generated by Django 5.0.1 on 2024-02-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('confirmPass', models.TextField()),
                ('mobilPhone', models.TextField()),
                ('photo', models.ImageField(upload_to='user/images')),
            ],
        ),
    ]
