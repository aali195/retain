# Generated by Django 2.1.7 on 2019-03-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='image',
            field=models.ImageField(null=True, upload_to='statements/%Y/%m'),
        ),
    ]
