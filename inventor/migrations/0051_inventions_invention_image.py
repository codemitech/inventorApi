# Generated by Django 4.0.4 on 2022-07-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0050_remove_inventions_gallery_inventions_inventor_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventions',
            name='invention_image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
