# Generated by Django 4.1 on 2022-08-13 13:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dosj9cjie/image/upload/v1660395826/default_vjewyn.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]
