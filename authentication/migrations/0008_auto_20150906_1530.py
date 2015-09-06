# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20150906_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
