# Generated by Django 3.2.9 on 2021-11-12 14:06

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FetchFile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file', models.FilePathField(path=pathlib.PurePosixPath('/files'))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
