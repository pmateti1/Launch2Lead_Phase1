# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Essential_Formats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('picture', models.ImageField(upload_to=b'static/images/blog')),
                ('body', models.TextField()),
                ('short_body', models.TextField(max_length=300)),
                ('posted_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Market_Research',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('picture', models.ImageField(upload_to=b'static/images/blog')),
                ('body', models.TextField()),
                ('short_body', models.TextField(max_length=300)),
                ('posted_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Published_Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('picture', models.ImageField(upload_to=b'static/images/blog')),
                ('body', models.TextField()),
                ('short_body', models.TextField(max_length=300)),
                ('posted_by', models.CharField(max_length=100)),
            ],
        ),
    ]
