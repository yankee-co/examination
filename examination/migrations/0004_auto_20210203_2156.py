# Generated by Django 3.1.4 on 2021-02-03 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0003_auto_20210203_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 21, 56, 9, 19283)),
        ),
    ]
