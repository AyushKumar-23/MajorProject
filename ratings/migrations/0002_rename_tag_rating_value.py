# Generated by Django 3.2.8 on 2024-05-04 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='tag',
            new_name='value',
        ),
    ]
