# Generated by Django 3.2.5 on 2021-09-11 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0002_auto_20210911_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetails',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='dob',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='emergency_contact1',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='emergency_contact2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='cust_email',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='password',
            field=models.CharField(default='', max_length=64),
        ),
    ]
