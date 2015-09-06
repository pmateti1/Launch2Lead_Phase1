# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
