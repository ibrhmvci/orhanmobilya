# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=250, verbose_name='Servis Adı')),
                ('content', models.TextField(verbose_name='Servis İçeriği')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=250, verbose_name='Servis Başlığı')),
                ('image', models.ImageField(upload_to='', verbose_name='Ana Resim (500x600)')),
            ],
        ),
    ]