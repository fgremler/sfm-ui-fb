# Generated by Django 2.0.7 on 2018-07-25 11:45

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0021_auto_20180712_1310'),
    ]

    operations = [
        migrations.RunSQL('drop table if exists apscheduler_jobs;')
    ]
