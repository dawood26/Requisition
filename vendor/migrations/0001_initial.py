# Generated by Django 2.0.4 on 2018-05-24 15:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=30)),
                ('p_created', models.DateTimeField(default=datetime.datetime(2018, 5, 24, 15, 14, 11, 578502))),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vn_name', models.CharField(max_length=30)),
                ('vn_phone', models.CharField(max_length=30)),
                ('vn_email', models.CharField(max_length=30)),
                ('vn_address', models.CharField(max_length=30)),
                ('vn_created', models.DateTimeField(default=datetime.datetime(2018, 5, 24, 15, 14, 11, 578042))),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='p_vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Vendor'),
        ),
    ]
