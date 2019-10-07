# Generated by Django 2.1.5 on 2019-10-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1, verbose_name='Порядок отображения')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='Картинка')),
                ('header', models.CharField(max_length=255, verbose_name='Заголовок банера')),
                ('text1', models.CharField(max_length=255, verbose_name='Текст 1')),
                ('text2', models.CharField(max_length=255, verbose_name='Текст 2')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать?')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
    ]
