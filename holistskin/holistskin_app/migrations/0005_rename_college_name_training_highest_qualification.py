# Generated by Django 5.0.2 on 2024-03-08 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holistskin_app', '0004_training_rename_timestamp_blogs_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='college_name',
            new_name='highest_qualification',
        ),
    ]
