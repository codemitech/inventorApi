# Generated by Django 4.0.4 on 2022-05-02 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0007_inventions_invention_name_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='investor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventor.investor'),
        ),
    ]
