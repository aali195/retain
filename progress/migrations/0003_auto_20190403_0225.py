# Generated by Django 2.1.7 on 2019-04-03 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0002_auto_20190312_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='progress',
            name='streak',
            field=models.IntegerField(default=0),
        ),
    ]
