# Generated by Django 4.0.4 on 2022-07-01 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0048_investor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='user',
        ),
        migrations.DeleteModel(
            name='inventor',
        ),
        migrations.DeleteModel(
            name='investor',
        ),
    ]
