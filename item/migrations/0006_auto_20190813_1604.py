# Generated by Django 2.1.5 on 2019-08-13 13:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20190813_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 13, 13, 4, 22, 185160, tzinfo=utc), verbose_name='Срок действия безлимитного кода'),
        ),
    ]