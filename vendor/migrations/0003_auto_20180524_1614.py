# Generated by Django 2.0.4 on 2018-05-24 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20180524_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 24, 16, 14, 6, 754558)),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vn_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 24, 16, 14, 6, 754214)),
        ),
    ]
