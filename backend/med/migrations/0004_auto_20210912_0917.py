# Generated by Django 3.2.4 on 2021-09-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0003_auto_20210911_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='dob',
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='age',
            field=models.IntegerField(default=30),
        ),
    ]
