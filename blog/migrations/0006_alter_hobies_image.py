# Generated by Django 5.0.2 on 2024-02-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobies',
            name='image',
            field=models.ImageField(upload_to='bloguygulama'),
        ),
    ]
