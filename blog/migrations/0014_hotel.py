# Generated by Django 5.0.2 on 2024-02-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_hobies_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='hotel_images/')),
            ],
        ),
    ]
