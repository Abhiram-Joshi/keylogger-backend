# Generated by Django 4.0.3 on 2022-04-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keylogger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbasedkeyloggermodel',
            name='website',
            field=models.URLField(max_length=100),
        ),
    ]