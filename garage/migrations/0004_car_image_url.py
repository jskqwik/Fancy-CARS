# Generated by Django 3.2.4 on 2021-06-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0003_rename_in_color_car_interior_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
