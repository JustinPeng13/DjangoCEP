# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0004_auto_20150713_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'pink', max_length=50)),
                ('fontcolor', models.CharField(default=b'green', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tag',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(related_name='grocery_list', null=True, to='grocery_list.Category', blank=True),
            preserve_default=True,
        ),
    ]
