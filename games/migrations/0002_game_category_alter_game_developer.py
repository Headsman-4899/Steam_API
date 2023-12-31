# Generated by Django 4.2.3 on 2023-07-28 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        ('developers', '0002_alter_developer_table'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='developers.developer'),
        ),
    ]
