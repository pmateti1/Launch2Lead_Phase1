# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_documents', '0002_auto_20151004_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='essential_format',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='market_research',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='published_post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
