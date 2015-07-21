# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0002_auto_20150718_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 21, 8, 13, 6, 405992, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
