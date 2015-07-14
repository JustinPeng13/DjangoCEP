# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='remarks',
            field=models.TextField(default='NIL', blank=True),
            preserve_default=False,
        ),
    ]
