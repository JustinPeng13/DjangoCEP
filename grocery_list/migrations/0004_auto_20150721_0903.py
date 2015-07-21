# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0003_auto_20150721_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cat',
            field=models.ManyToManyField(related_name='grocery_list', to='grocery_list.Cat', blank=True),
            preserve_default=True,
        ),
    ]
