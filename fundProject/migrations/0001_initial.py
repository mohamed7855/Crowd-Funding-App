# Generated by Django 5.0.1 on 2024-02-19 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='CommentReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundProject.comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=285)),
                ('details', models.TextField()),
                ('totalTarget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('startTime', models.DateTimeField(auto_now=True)),
                ('endTime', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fundProject.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='fundProject/images')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundProject.project')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_value', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundProject.project')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundProject.project'),
        ),
        migrations.CreateModel(
            name='ProjectReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundProject.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundProject.project')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=40)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundProject.project')),
            ],
        ),
    ]
