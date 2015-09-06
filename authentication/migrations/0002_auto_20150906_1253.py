# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=b'email', unique=True, max_length=254, verbose_name=b'email address'),
        ),
    ]
