# Generated by Django 4.0.4 on 2022-05-02 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0014_investment_invention'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='Invention',
        ),
        migrations.AddField(
            model_name='investment',
            name='is_investor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
