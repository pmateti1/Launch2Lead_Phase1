# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Launch2Lead_v01', '0007_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('picture', models.ImageField(upload_to=b'', db_index=True)),
                ('body', models.TextField()),
                ('short_body', models.TextField()),
                ('posted_by', models.CharField(unique=True, max_length=100)),
            ],
        ),
    ]
