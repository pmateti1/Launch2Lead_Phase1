# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_documents', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Essential_Formats',
            new_name='Essential_Format',
        ),
        migrations.RenameModel(
            old_name='Published_Posts',
            new_name='Published_Post',
        ),
    ]
