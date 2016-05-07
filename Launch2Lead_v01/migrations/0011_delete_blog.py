# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Launch2Lead_v01', '0010_blog_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
