# Generated by Django 5.1.4 on 2025-01-08 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('title_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'titles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ViewingActivity',
            fields=[
                ('profile_name', models.CharField(blank=True, max_length=50, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('video_type', models.CharField(blank=True, max_length=255, null=True)),
                ('device_type', models.CharField(blank=True, max_length=255, null=True)),
                ('latest_bookmark', models.CharField(blank=True, max_length=255, null=True)),
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'viewing_activity',
                'managed': False,
            },
        ),
    ]
