# Generated by Django 4.2.3 on 2023-07-28 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_country_alter_user_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 28, 11, 18, 22, 956967, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_time_online',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 28, 11, 18, 22, 956967, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 28, 11, 18, 22, 956967, tzinfo=datetime.timezone.utc)),
        ),
    ]
