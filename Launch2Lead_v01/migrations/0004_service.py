# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Launch2Lead_v01', '0003_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(unique=True, max_length=128)),
                ('Description', models.TextField()),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
            ],
        ),
    ]
