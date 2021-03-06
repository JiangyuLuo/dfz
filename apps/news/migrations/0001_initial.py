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
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('contetn', models.TextField(verbose_name='\u5185\u5bb9')),
                ('desc', models.CharField(max_length=200, verbose_name='\u7b80\u77ed\u63cf\u8ff0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('thumbnail', models.URLField(verbose_name='\u7f29\u7565\u56fe')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7c7b\u540d')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u5206\u7c7b',
                'verbose_name_plural': '\u65b0\u95fb\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='\u65b0\u95fb')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u8bc4\u8bba',
                'verbose_name_plural': '\u65b0\u95fb\u8bc4\u8bba',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewsCategory', verbose_name='\u5206\u7c7b'),
        ),
    ]
