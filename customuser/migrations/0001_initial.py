# Generated by Django 2.1.5 on 2019-09-15 19:45

import customuser.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Эл. почта')),
                ('is_vip', models.BooleanField(default=False, verbose_name='Вип?')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('family', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('otchestvo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('post_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Индекс')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('passport', models.CharField(blank=True, max_length=255, null=True, verbose_name='Паспортные данные')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к пользователю(видно только админу)')),
                ('is_allow_email', models.BooleanField(default=True, verbose_name='Согласен на рассылку')),
                ('is_use_promo', models.BooleanField(default=False, verbose_name='Использовал промо-код?')),
                ('bonuses', models.DecimalField(blank=True, db_index=True, decimal_places=2, default=0, max_digits=6, verbose_name='Бонусы')),
                ('profile_ok', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('used_promo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.PromoCode', verbose_name='Использованный промо-код при текущей корзине')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', customuser.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ключ сессии')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Эл. почта')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('family', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('otchestvo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('post_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Индекс')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('passport', models.CharField(blank=True, max_length=255, null=True, verbose_name='Паспортные данные')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('used_promo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.PromoCode', verbose_name='Использованный промо-код при текущей корзине')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', verbose_name='Отзыв')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='Отзыв о товаре')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отзыв от')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
