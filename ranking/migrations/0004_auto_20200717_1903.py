# Generated by Django 3.0.8 on 2020-07-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0003_auto_20200617_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]