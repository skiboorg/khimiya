# Generated by Django 2.1.5 on 2019-10-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bonuses',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Бонусы'),
        ),
    ]
