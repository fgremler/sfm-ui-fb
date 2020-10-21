# Generated by Django 2.0.9 on 2018-12-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0022_auto_20180725_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='export_segment_size',
            field=models.BigIntegerField(blank=True, choices=[(100000, '100,000'), (250000, '250,000'), (500000, '500,000'), (1000000, '1,000,000'), (None, 'Single file')], default=250000, null=True),
        ),
    ]
