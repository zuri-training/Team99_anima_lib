# Generated by Django 4.1 on 2022-08-13 14:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=cloudinary.models.CloudinaryField(default='\\staticfiles\x07ccounts\\default.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]
