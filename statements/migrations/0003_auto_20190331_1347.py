# Generated by Django 2.1.7 on 2019-03-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statements', '0002_auto_20190331_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='image',
            field=models.ImageField(blank=True, upload_to='statements/%Y/%m'),
        ),
    ]
