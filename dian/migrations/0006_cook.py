# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dian', '0005_auto_20151201_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cook_user', models.CharField(max_length=10, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('cook_pas', models.CharField(max_length=10, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
    ]
