# Generated by Django 5.0.2 on 2024-02-17 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_hobies_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobies',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
