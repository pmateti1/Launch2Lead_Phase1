# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Launch2Lead_v01', '0009_auto_20151002_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=1, max_length=100, choices=[(b'1', b'Market Research'), (b'2', b'Published Post'), (b'3', b'Essential Formats')]),
            preserve_default=False,
        ),
    ]
