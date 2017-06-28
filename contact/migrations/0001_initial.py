# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Adres')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Telefon numarası')),
                ('mobile_number', models.CharField(max_length=11, verbose_name='Mobil Numara')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail Adresi')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('google_plus', models.URLField(verbose_name='Google Plus')),
                ('linked_in', models.URLField(verbose_name='Linkedin')),
                ('tumblr', models.URLField(verbose_name='Tumblr')),
            ],
        ),
    ]
