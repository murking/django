# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_room', models.PositiveIntegerField(verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7')),
                ('customer_dishs', models.CharField(max_length=45, verbose_name=b'\xe8\x8f\x9c\xe8\xa1\xa8')),
                ('customer_sum', models.PositiveIntegerField(verbose_name=b'\xe6\x80\xbb\xe4\xbb\xb7')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dish_id', models.PositiveIntegerField(verbose_name=b'\xe8\x8f\x9c\xe5\x93\x81\xe5\x8f\xb7')),
                ('dish_name', models.CharField(max_length=45, verbose_name=b'\xe8\x8f\x9c\xe5\x90\x8d')),
                ('dish_imag', models.FileField(upload_to=b'images/', max_length=255, verbose_name=b'\xe8\x8f\x9c\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87')),
            ],
        ),
    ]
