# Generated by Django 3.0.3 on 2020-02-21 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0007_auto_20200221_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controlpanel',
            old_name='profile',
            new_name='profile_name',
        ),
    ]
