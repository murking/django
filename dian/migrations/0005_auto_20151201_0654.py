# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dian', '0004_auto_20151127_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_room',
            field=models.CharField(max_length=10, verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7'),
        ),
    ]
