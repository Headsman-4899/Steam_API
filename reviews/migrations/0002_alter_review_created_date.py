# Generated by Django 4.2.3 on 2023-07-28 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 28, 11, 18, 22, 958967, tzinfo=datetime.timezone.utc)),
        ),
    ]