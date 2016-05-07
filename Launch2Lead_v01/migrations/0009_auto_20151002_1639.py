# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Launch2Lead_v01', '0008_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.ImageField(upload_to=b'static/images/blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_body',
            field=models.TextField(max_length=300),
        ),
    ]
