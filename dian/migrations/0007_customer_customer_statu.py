# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dian', '0006_cook'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_statu',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=False,
        ),
    ]
