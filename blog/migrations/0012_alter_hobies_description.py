# Generated by Django 5.0.2 on 2024-02-18 22:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_hobies_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobies',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]