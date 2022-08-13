# Generated by Django 4.0.4 on 2022-07-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0049_remove_investor_user_delete_inventor_delete_investor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventions',
            name='gallery',
        ),
        migrations.AddField(
            model_name='inventions',
            name='inventor_image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='inventions',
            name='inventor_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]