# Generated by Django 4.2.3 on 2023-07-11 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_remove_post_timestamp_post_imestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imestamp',
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 10, 21, 44, 910509, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='likes',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 10, 21, 44, 910796, tzinfo=datetime.timezone.utc)),
        ),
    ]
