# Generated by Django 3.2.8 on 2022-04-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0002_auto_20220418_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventor',
            name='is_inventor',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='is_investor',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
