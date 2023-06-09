# Generated by Django 3.1.5 on 2023-06-08 04:19

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOperateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='人员')),
                ('scope', models.CharField(max_length=20, verbose_name='操作范围')),
                ('type', models.CharField(max_length=20, verbose_name='操作类型')),
                ('content', models.IntegerField(verbose_name='操作内容')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='操作时间')),
            ],
            options={
                'verbose_name': '用户操作日志',
                'verbose_name_plural': '用户操作日志',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('staff_no', models.CharField(blank=True, max_length=15, verbose_name='工号')),
                ('department', models.CharField(blank=True, max_length=15, verbose_name='部门')),
                ('isadmin', models.CharField(blank=True, choices=[('1', '是'), ('0', '否')], default='0', max_length=10, verbose_name='是否管理员')),
                ('bg_telephone', models.CharField(blank=True, max_length=12, verbose_name='办公电话')),
                ('mobile', models.CharField(blank=True, max_length=11, verbose_name='手机号码')),
                ('is_superuser', models.IntegerField(default=0, verbose_name='是否超级管理员')),
                ('is_staff', models.CharField(blank=True, choices=[('1', '是'), ('0', '否')], default='1', max_length=10, verbose_name='是否在职')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
