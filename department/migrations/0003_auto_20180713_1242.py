# Generated by Django 2.0.7 on 2018-07-13 12:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_auto_20180713_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeuser',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.gender'),
        ),
        migrations.AlterField(
            model_name='employeeuser',
            name='emp_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 12, 42, 46, 15379, tzinfo=utc)),
        ),
    ]
