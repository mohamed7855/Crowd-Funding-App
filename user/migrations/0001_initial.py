
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
                ('firstName', models.IntegerField()),
                ('lastName', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('confirmPass', models.TextField()),
                ('mobilPhone', models.TextField()),
                ('photo', models.TextField()),
            ],
        ),
    ]