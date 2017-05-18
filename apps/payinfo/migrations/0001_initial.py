# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u8d44\u8baf\u540d\u79f0')),
                ('profile', models.TextField(verbose_name='\u8d44\u8baf\u7b80\u4ecb')),
                ('price', models.FloatField(default=0, verbose_name='\u4ef7\u683c(\u5143/\u6b21)')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4ed8\u8d39\u8d44\u8baf',
                'verbose_name_plural': '\u4ed8\u8d39\u8d44\u8baf',
            },
        ),
        migrations.CreateModel(
            name='PayinfoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5206\u7c7b\u540d')),
            ],
            options={
                'verbose_name': '\u4ed8\u8d39\u8d44\u8baf\u5206\u7c7b',
                'verbose_name_plural': '\u4ed8\u8d39\u8d44\u8baf\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='UserPayinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8d2d\u4e70\u65f6\u95f4')),
                ('payinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payinfo.Payinfo', verbose_name='\u8d44\u8baf')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u8d44\u8baf\u8d2d\u4e70\u8bb0\u5f55',
                'verbose_name_plural': '\u8d44\u8baf\u8d2d\u4e70\u8bb0\u5f55',
            },
        ),
        migrations.AddField(
            model_name='payinfo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payinfo.PayinfoCategory', verbose_name='\u5206\u7c7b'),
        ),
    ]
