# Generated by Django 5.1.4 on 2025-01-11 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrapped_app', '0003_viewingactivity_title_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewingactivity',
            name='title_id',
        ),
    ]
