# Generated by Django 3.2.8 on 2024-05-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_alter_rating_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.IntegerField(blank=True, choices=[(None, 0), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], null=True),
        ),
    ]
