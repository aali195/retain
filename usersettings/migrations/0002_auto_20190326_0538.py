# Generated by Django 2.1.7 on 2019-03-26 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
        ('usersettings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='active_collection',
        ),
        migrations.AddField(
            model_name='usersettings',
            name='active_sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='subscriptions.Subscription'),
        ),
    ]
