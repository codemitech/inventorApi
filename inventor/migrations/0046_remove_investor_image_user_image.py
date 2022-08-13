# Generated by Django 4.0.4 on 2022-06-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0045_remove_investor_company_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='image',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]