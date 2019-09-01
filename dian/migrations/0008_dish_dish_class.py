# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dian', '0007_customer_customer_statu'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_class',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
            preserve_default=False,
        ),
    ]
