# Generated by Django 5.0.2 on 2024-02-18 21:51

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_hobies_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobies',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
    ]
