# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to=b'static/images/customer-pic')),
                ('posted_by', models.CharField(max_length=100)),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('category', models.IntegerField(choices=[(b'1', b'Jobs Posting'), (b'2', b'Buy/Sell Products'), (b'3', b'Networking')])),
            ],
        ),
    ]
