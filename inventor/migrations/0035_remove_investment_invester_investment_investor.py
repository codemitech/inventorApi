# Generated by Django 4.0.4 on 2022-05-07 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0034_remove_investment_user_investment_invester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='invester',
        ),
        migrations.AddField(
            model_name='investment',
            name='investor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
