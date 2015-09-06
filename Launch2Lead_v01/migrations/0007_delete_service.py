# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Launch2Lead_v01', '0006_auto_20150905_1935'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
    ]
