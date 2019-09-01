# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dian', '0003_auto_20151127_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_name',
            field=models.CharField(max_length=2000, null=True, verbose_name=b'\xe8\x8f\x9c\xe5\x90\x8d'),
        ),
    ]
