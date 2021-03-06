# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail Adresi'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobil Numara'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefon numarası'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='google_plus',
            field=models.URLField(blank=True, null=True, verbose_name='Google Plus'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='linked_in',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='tumblr',
            field=models.URLField(blank=True, null=True, verbose_name='Tumblr'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter'),
        ),
    ]
