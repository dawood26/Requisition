# Generated by Django 2.0.4 on 2018-05-24 16:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0002_auto_20180524_1607'),
        ('department', '0008_auto_20180524_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=30)),
                ('unitprice', models.FloatField()),
                ('totalprice', models.FloatField()),
                ('instructution', models.CharField(max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 5, 24, 16, 7, 47, 369082))),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Product')),
                ('requisitioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Employee')),
            ],
        ),
    ]
