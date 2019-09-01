# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dian', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_price',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc'),
            preserve_default=False,
        ),
    ]
